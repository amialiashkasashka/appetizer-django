from django.contrib import admin
from .models import Booking, Contact

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'phone')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'header')    

admin.site.register(Contact, ContactAdmin)
admin.site.register(Booking, BookingAdmin)   