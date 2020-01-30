from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from rest_framework import viewsets

from .models import Bike
from .serializers import BikeSerializer

# Create your views here.

def index(request):
    all_bikes = Bike.objects.all()
    context = {
        'all_bikes': all_bikes
    }

    return render(request, 'index.html', context)


class BikeView(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer