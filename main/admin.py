from django.contrib import admin
from .models import Category, Menu, Chefs

# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_published', 'is_on_home_page')
    list_editable = ('is_published', 'is_on_home_page')


admin.site.register(Category)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Chefs)
