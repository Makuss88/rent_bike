from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Client)
class ViewAdmin(ImportExportModelAdmin):
    pass
