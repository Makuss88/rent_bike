from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from .models import Bike
from bike.serializers import BikeSerializer

# Create your views here.

def index(request):
    all_bikes = Bike.objects.all()
    context = {
        'all_bikes': all_bikes
    }

    return render(request, 'bike.html', context)

class BikeView(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer