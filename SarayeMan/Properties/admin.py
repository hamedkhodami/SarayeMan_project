from django.contrib import admin
from .models import PropertyModel
# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title","price","date_posted","property_type","user")



admin.site.register(PropertyModel,PropertyAdmin)