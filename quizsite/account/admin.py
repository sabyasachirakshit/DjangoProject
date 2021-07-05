from django import forms
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Profile

# Register your models here.
@admin.register(Profile)


class ViewAdmin(ImportExportModelAdmin):
    pass
