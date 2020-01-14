from django.db import models
from django import forms

# Create your models here.

class Bike(models.Models):

    number_bike = models.IntegerField()
    color_bike = models.CharField(max_length='20')
    is_free = models.BooleanField(default=True)

    def __str__(self):
        return self.number_bike, 'and his color is', self.color_bike

class User(forms.Form):

    first_name = models.CharField(max_length='50')
    last_name = models.CharField(max_length='100')
    email = models.EmailField(max_length='256')
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)
    wallet = models.IntegerField

    def __str__(self):
        return self.last_name, self.first_name