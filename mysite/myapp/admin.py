from django.contrib import admin
from .models import Book1
from import_export.admin import ImportExportModelAdmin


@admin.register(Book1)
class userdata(ImportExportModelAdmin):
    pass
