from rest_framework import serializers
from .models import Bike


class BikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bike
        #fields = ("number_bike", "color_bike", "is_free", "image")
        fields = '__all__'