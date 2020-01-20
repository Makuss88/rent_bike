from django.shortcuts import render
from .models import Bike
from rest_framework import generics
from .serializers import BikeSerializer

# Create your views here.

class ListBikeView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer

def index(request):
    all_bikes = Bike.objects.all()
    context = {
        'all_bikes': all_bikes
    }

    return render(request, 'index.html', context)