from django.contrib import admin
from .models import Blog

# Register your models here.

class BloggingAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'list_date')
    list_editable = ('is_published')

admin.site.register(Blog)    