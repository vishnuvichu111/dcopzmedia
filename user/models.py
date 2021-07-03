from django.db import models


# Create your models here.

class imggal(models.Model):
    image = models.ImageField(upload_to='media/static/images/')


class enquiry(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    message = models.CharField(max_length=250, null=True, blank=True)


