from django.contrib import admin
from .models import ContactUS
# Register your models here.

class ContactsAdmin(admin.ModelAdmin):
    list_display = ("Fullname","Email","created_at")



admin.site.register(ContactUS,ContactsAdmin)
