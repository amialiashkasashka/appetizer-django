from django.shortcuts import render, redirect
from .models import Booking, Contact, subscribtion
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail

# Create your views here.
def booking(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        guests = request.POST['guests']

        booking = Booking(name=name, email=email, phone=phone, date=date, time=time, guests=guests)
        booking.save()

        # send mail
        send_mail(
            'Booking Inquiry',
            f'{ name } wants to book a table for ' + guests + ' guests on ' + date + ' at ' + time + '. Phone number - ' + phone + '. Sign into the admin panel for more info.',
            'sanyok200092@gmail.com',
            ['a.amialiashka@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, 'Great! The table is now yours.')

        return redirect('reservation')

def contacting(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        header = request.POST['header']
        message = request.POST['message']

        contact = Contact(name=name, email=email, header=header, message=message)
        contact.save()
        
        # send mail
        send_mail(
            f'{header}',
            f'From {name}. {message} \n {email}',
            'sanyok200092@gmail.com',
            ['a.amialiashka@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, 'Thanks for your message!')

        return redirect('contact')


def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']

        sub = subscribtion(email=email)
        sub.save()

        messages.success(request, 'Thanks, sub!')
        return redirect('index')



def mailing(request):

    subscribers = subscribtion.objects.all()
    arr = list(subscribers) 

    if request.method == 'POST':
        message = request.POST['message']

        send_mail(
            'It`s Appetizer!',
            f'{message}',
            'sanyok200092@gmail.com',
            arr,
            fail_silently=False,
        )  

        return redirect('/admin')    