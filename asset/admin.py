from django.contrib import admin
from   asset.models import  Host

# Register your models here.
class hostadmin(admin.ModelAdmin):
        list_display = ('hostname','ipaddres','manage_user','port','yw','type_choice','status','c_time')
        search_fields = ('hostname','ipaddres',)

admin.site.register(Host,hostadmin)
