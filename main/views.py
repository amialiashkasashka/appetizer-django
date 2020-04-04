from django.shortcuts import render
from django.conf import settings

from .models import Menu, Category, Chefs

# Create your views here.
def index(request):

    menus = Menu.objects.all().filter(is_on_home_page=True) 
    chefs = Chefs.objects.all()
    categories = Category.objects.all()

    context = {
        'chefs': chefs,
        'menus': menus,
        'categories': categories,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    menus = Menu.objects.all().filter(is_on_home_page=True) 
    chefs = Chefs.objects.all()

    context = {
        'chefs': chefs,
        'menus': menus,
    }
    return render(request, 'pages/about.html', context)

def menu(request):
    return render(request, 'pages/menu.html') 


def reservation(request):
    return render(request, 'pages/reservation.html')