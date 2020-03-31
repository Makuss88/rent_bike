from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'', include('bike.urls')),
    path(r'accounts/', include('accounts.urls')),
    path(r'admin/', admin.site.urls),
]