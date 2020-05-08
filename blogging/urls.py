from django.urls import path, include
from . import views


urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blogsingle/<int:id>/', views.blogsingle, name='blogsingle'),
    path('search/', views.search, name='search'),
    path('tag_search/', views.tag_search, name='tag_search')
]