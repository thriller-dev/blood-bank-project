from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Donor
from .forms import DonorRegistrationForm

def home(request):
    blood_groups = Donor.BLOOD_GROUP_CHOICES
    return render(request, 'donors/home.html', {'blood_groups': blood_groups})

def register_donor(request):
    if request.method == 'POST':
        form = DonorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for registering as a blood donor!')
            return redirect('home')
    else:
        form = DonorRegistrationForm()
    return render(request, 'donors/register.html', {'form': form})

def search_results(request):
    query_bg = request.GET.get('blood_group')
    query_city = request.GET.get('city')
    
    donors = Donor.objects.filter(is_available=True)
    
    if query_bg:
        donors = donors.filter(blood_group=query_bg)
    if query_city:
        donors = donors.filter(city__icontains=query_city)
        
    donors = donors.order_by('-created_at')
    
    return render(request, 'donors/results.html', {
        'donors': donors,
        'query_bg': query_bg,
        'query_city': query_city
    })

def about(request):
    return render(request, 'donors/about.html')

def contact(request):
    return render(request, 'donors/contact.html')
