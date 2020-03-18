from rest_framework import viewsets

from .models import Client
from .serializers import ClientSerializer


class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
