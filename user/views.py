from django.shortcuts import render


# Create your views here.
from .models import *


def index(request):
    return render(request, 'index.html')

def pricing(request):
    return render(request, 'pricing.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        db = enquiry(name=name, email=email, phone=phone, message=message)
        print(db)
        db.save()
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def gallery(request):
    image=imggal.objects.all()
    return render(request, 'gallery.html',{'imggal':image})
