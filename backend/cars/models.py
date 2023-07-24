from django.db import models
from django.conf import settings 

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=70)
    model = models.CharField(max_length=70)
    version = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=70)
    year = models.CharField(max_length=70)
    gear = models.CharField(max_length=70)
    fuel = models.CharField(max_length=70)
    mileage = models.CharField(max_length=70)
    power = models.CharField(max_length=70)
    optionals = models.TextField()
    description = models.TextField()
    created_at = models.DateField(auto_now=True)
    miniature = models.FileField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    showcase = models.BooleanField(default=False)

    def __str__(self):
        return self.make + " " + self.model 



class CompanyInfo(models.Model):
    address = models.CharField(max_length=300)
    phoneNumber = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    idCode = models.CharField(max_length=100)

    def __str__(self):
        return 'company-informations'