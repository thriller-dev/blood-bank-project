from django.contrib import admin
from .models import Donor

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'blood_group', 'city', 'phone_number', 'is_available')
    list_filter = ('blood_group', 'is_available', 'city')
    search_fields = ('full_name', 'city', 'phone_number')

