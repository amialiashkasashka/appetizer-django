from django.urls import path

from . import views

urlpatterns = [
    path('booking', views.booking, name='booking'),
    path('contacting', views.contacting, name='contacting'),
    path('mailing', views.mailing, name='mailing'),
    path('subscription', views.subscribe, name='subscription'),
]