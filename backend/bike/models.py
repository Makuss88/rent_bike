from django.db import models

class Bike(models.Model):

    COLOR_CHOICE = [
        ('BLACK', 'Black'),
        ('RED', 'Red'),
        ('WHITE', 'White'),
    ]

    number_bike = models.CharField(max_length=10000)
    color_bike = models.CharField(max_length=5, choices=COLOR_CHOICE)
    is_free = models.BooleanField(default=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        flag_borrow = 'borrow'
        if self.is_free:
            flag_borrow = 'free'
        return "bike no. " + self.number_bike + " - it's " + flag_borrow


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=128)
    wallet = models.IntegerField(default=0)

    def __str__(self):
        return self.last_name + ' ' + self.first_name