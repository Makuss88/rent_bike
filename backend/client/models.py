from django.db import models


class Client(models.Model):

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} is in our portal at {}".format(self.email, self.date)

