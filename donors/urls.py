from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_donor, name='register_donor'),
    path('results/', views.search_results, name='search_results'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
