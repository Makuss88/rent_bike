from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('bike.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls'))
]
