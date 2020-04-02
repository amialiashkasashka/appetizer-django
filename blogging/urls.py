from django.urls import path, include
from . import views


urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blogsingle/<int:id>/', views.blogsingle, name='blogsingle')
]