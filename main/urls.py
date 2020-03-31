from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index' ),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('blog/', views.blog, name='blog'),
]