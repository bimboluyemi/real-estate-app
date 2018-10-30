from django.db import models


class Country(models.Model):
    COUNTRY_CHOICES = ()
    countryName = models.CharField(max_length=25)

    def __str__(self):
        return self.countryName


class Province(models.Model):
    PROVINCE_CHOICES = ()
    provinceName = models.CharField(max_length=25)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.provinceName


class City(models.Model):
    cityName = models.CharField(max_length=25)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.cityName
