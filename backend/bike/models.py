from django.db import models


class Bike(models.Model):

    COLOR_CHOICE = [
        ('BLACK', 'Black'),
        ('RED', 'Red'),
        ('WHITE', 'White'),
    ]

    number_bike = models.IntegerField(unique=True)
    color_bike = models.CharField(max_length=5, choices=COLOR_CHOICE)
    is_free = models.BooleanField(default=True)
    image = models.CharField(max_length=500)

    def __str__(self):
        flag_borrow = 'borrow'
        if self.is_free:
            flag_borrow = 'free'
        return "bike no. {} - it's {}".format(self.number_bike, flag_borrow)
