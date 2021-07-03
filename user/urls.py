from django import views
from django.urls import path

from . import views
from .views import *


urlpatterns = [

    path('index/', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('pricing/', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
]
