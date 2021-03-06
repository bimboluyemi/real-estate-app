from django.db import models
import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Property(models.Model):
    propertyTitle = models.CharField(max_length=100)
    propertyCategory = models.ForeignKey('PropertyCategory', on_delete=models.CASCADE)
    propertySector = models.ForeignKey('PropertySector', on_delete=models.CASCADE)
    propertyFacing = models.ForeignKey('PropertyFacing', on_delete=models.CASCADE)
    propertyCountry = models.ForeignKey('Country', on_delete=models.CASCADE)
    propertyProvince = models.ForeignKey('Province', on_delete=models.CASCADE)
    propertyCity = models.ForeignKey('City', on_delete=models.CASCADE)
    propertyStreet = models.CharField(max_length=50)
    propertyPostalCode = models.CharField(max_length=6)
    propertyStreetNumber = models.CharField(max_length=5)
    propertyConstructionDate = models.DateField()
    propertyRegistrationDate = models.DateField()
    propertyNumberOfHalls = models.IntegerField()
    propertyNumberOfRooms = models.IntegerField()
    propertyNumberOfBathrooms = models.FloatField()
    propertyNumberOfFloors = models.IntegerField()
    propertyTotalArea = models.FloatField()
    propertyAskingPrice = models.FloatField()
    propertySellingPrice = models.FloatField()

    def __str__(self):
        return self.propertyTitle


class PropertyCategory(models.Model):
    PROPERTY_CATEGORY = (
        ('Single House', 'Single House'),
        ('Attached House', 'Attached House'),
        ('Town House', 'Town House'),
        ('Apartment', 'Apartment'),
        ('Store', 'Store'),
        ('Farm', 'Farm'),
        ('Factory', 'Factory'),
        ('Mall', 'Mall'),
        ('Building', 'Building'),
        ('Other', 'Other')
    )
    propertyCategory = models.CharField(max_length=20, choices=PROPERTY_CATEGORY)

    def __str__(self):
        return self.propertyCategory


class PropertySector(models.Model):
    PROPERTY_SECTOR = (
        ('Private', 'Private'),
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Government', 'Government'),
        ('Rural', 'Rural'),
        ('Other', 'Other')
    )
    propertySector = models.CharField(max_length=20, choices=PROPERTY_SECTOR)

    def __str__(self):
        return self.propertySector


class PropertyFacing(models.Model):
    PROPERTY_FACING = (
        ('North', 'North'),
        ('South', 'South'),
        ('East', 'East'),
        ('West', 'West'),
        ('Other', 'Other')
    )
    propertyFacing = models.CharField(max_length=10, choices=PROPERTY_FACING)

    def __str__(self):
        return self.propertyFacing


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    propertyImageDescription = models.CharField(max_length=100)
    propertyImage = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.propertyImageDescription

