from django.contrib import admin
from .models import Blog, Tag, Comment

# Register your models here.

class BloggingAdmin(admin.ModelAdmin):
    list_display    = ('title', 'author', 'is_published', 'list_date')
    list_editable   = ('is_published')

class CommentAdmin(admin.ModelAdmin):
    list_display    = ('name', 'created_on', 'email')
    list_filter     = ('created_on',)
    search_fields   = ('name', 'email', 'message')

admin.site.register(Blog)  
admin.site.register(Tag)  
admin.site.register(Comment, CommentAdmin)