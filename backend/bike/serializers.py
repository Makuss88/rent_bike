from rest_framework import serializers
from .models import Bike


class BikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bike
        fields = '__all__'
