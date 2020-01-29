from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Bike
from .serializers import BikeSerializer

# Create your views here.

def index(request):
    all_bikes = Bike.objects.all()
    context = {
        'all_bikes': all_bikes
    }

    return render(request, 'index.html', context)


class ListBikeView(APIView):

    def get(self, request):
        bike = Bike.objects.all()
        serializer = BikeSerializer(bike, many=True)
        return Response(serializer.data)
