from django.shortcuts import render
from .models import Bike, User

# Create your views here.
def index(request):
    all_bikes = Bike.objects.all()
    url = 'index.html'
    context = {
        'all_bikes': all_bikes
    }

    return render(request, url, context)