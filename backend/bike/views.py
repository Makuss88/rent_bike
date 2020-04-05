from rest_framework import viewsets

from .models import Bike
from .serializers import BikeSerializer


class BikeView(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
