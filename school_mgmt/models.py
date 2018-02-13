from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import serializers

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
       Token.objects.create(user=instance)


class University(models.Model):

    # name (Charfield, mandatory)
    # logo (mandatory)
    # website (optional)
    # created_at
    # modified_at
    # is_active (default-True)
    name = models.CharField(max_length=200)
    Logo = models.ImageField(upload_to='logo_images/')
    website = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    school_count = serializers.IntegerField(source='school_set.count', read_only=True)

    

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"
        

    def __str__(self):
        return self.name

class School(models.Model):

    # School
    # ******
    # owner(FK(user)) (mandatory)
    # university(FK) (mandatory)
    # name (Charfield, mandatory)
    # logo (mandatory)
    # website (optional)
    # created_at
    # modified_at
    # is_active (default=True)


    # creator = models.ForeignKey(User, related_name='schools')
    owner = models.ForeignKey(User, related_name='schools')
    university = models.ForeignKey(University, related_name='school')
    name = models.CharField(max_length=200)
    Logo = models.ImageField(upload_to='logo_images/')
    website = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
        

    def __str__(self):
        return self.name


class Address(models.Model):

    # Address
    # *******
    # street_1 (Char, mandatory)
    # street_2 (Char, mandatory)
    # city (Char, mandatory)
    # state (Char, mandatory)
    # country (Choices: (Any 5 countries))
    # zipcode (number, optional)
    # mobile (number, optional)
    country = (
            ('india', 'India'),
            ('us', 'UnitedState'), 
            ('austrelia', 'Austrelia'),
            ('pakistan', 'Pakistan'), 
            ('africa', 'Africa'),
        )
    street_1 = models.CharField(max_length=50)
    street_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(choices=country, max_length=10)
    zipcode = models.IntegerField(max_length=20)
    mobile = models.IntegerField(max_length=50)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Address"
        


    def __str__(self):
        return self.street_1 + self.street_2 + self.city + self.state

class Student(models.Model):

    # Student
    # *******
    # SMARTNumber(auto generate)
    # school(FK) (mandatory)
    # first_name (mandatory)
    # last_name (mandatory)
    # roll_number (number, mandatory)
    # email (email field, mandatory)
    # date_of_birth(Charfield, mandatory)
    # address (ManytoMany, optional)
    # created_date
    # modified_at
    # is_active (default=True)

        # country = (
        # 		('india', 'India'),
        # 		('us', 'UnitedState'), 
        # 		('austrelia', 'Austrelia'),
        #         ('pakistan', 'Pakistan'), 
        # 		('africa', 'Africa'),
        # 	)
    SMARTNumber = models.CharField(max_length=20, blank=True, null=True)
    school = models.ForeignKey(School, related_name='school_name')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_number = models.IntegerField(max_length=50)
    email = models.EmailField(max_length=200)
    date_of_birth = models.CharField(max_length=100)
    address = models.ManyToManyField(Address)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
        
        


    def __str__(self):
        return self.first_name 

