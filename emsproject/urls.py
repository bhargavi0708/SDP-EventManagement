"""
URL configuration for emsproject project.
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homefunction, name='home'),
    path('about/', views.aboutfunction, name='about'),
    path('login/', views.loginfunction, name='login'),
    path('contact/', views.contactfunction, name='contact'),
    path('', include('adminapp.urls')),
    path('', include('staffapp.urls')),
    path('', include('coordinatorapp.urls')),
]
