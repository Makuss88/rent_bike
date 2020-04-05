from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)


urlpatterns = [
    path('register', views.register, name="register"),
    path('', include(router.urls)),
]
