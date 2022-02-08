from django.contrib import admin
from .models import Book1
from .models import Hospital_beds
from .models import District
from import_export.admin import ImportExportModelAdmin


@admin.register(Book1)
class userdata(ImportExportModelAdmin):
    pass
@admin.register(Hospital_beds)
class userdata(ImportExportModelAdmin):
    pass

@admin.register(District)
class userdata(ImportExportModelAdmin):
    pass


def sl(request):
    st=District.objects.all() # Collect all records from table
    return render(request,'local.html',{'st':st})

