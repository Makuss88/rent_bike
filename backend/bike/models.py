from django.db import models

class Bike(models.Model):

    number_bike = models.CharField(max_length=10000)
    color_bike = models.CharField(max_length=10)
    is_free = models.BooleanField(default=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        extra = ''
        if self.is_free:
            extra = " - it's free"
        return "bike no. " + self.number_bike + ' ' + extra


class User(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=128)
    wallet = models.IntegerField(default=0)

    def __str__(self):
        return self.last_name + ' ' + self.first_name