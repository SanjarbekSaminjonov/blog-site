from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):

    regions = [
        ('1', 'Andijon viloyati'),
        ('2', 'Buxoro viloyati'),
        ('3', 'Farg\'ona viloyati'),
        ('4', 'Jizzax viloyati'),
        ('5', 'Xorazm viloyati'),
        ('6', 'Namangan viloyati'),
        ('7', 'Navoiy viloyati'),
        ('8', 'Qashqadaryo'),
        ('9', 'Qoraqalpog\'iston Respublikasi'),
        ('10', 'Samarqand viloyati'),
        ('11', 'Sirdaryo viloyati'),
        ('12', 'Surxondaryo'),
        ('13', 'Toshkent viloyati'),
        ('14', 'Toshkent shahri')
    ]

    email = models.EmailField(blank=True, unique=True)
    mobile = models.CharField(max_length=15, default='+998', unique=True)
    region = models.CharField(
        max_length=35,
        choices=regions,
        default='14'
    )

    def get_region(self):
        return dict(CustomUser.regions)[self.region]
