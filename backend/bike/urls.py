from django.urls import path
from . import views
from .views import ListBikeView


urlpatterns = [
    path('', views.index, name='index'),
    path('bike/', ListBikeView.as_view(), name="bikes-all")
]