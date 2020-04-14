from django.shortcuts import render, redirect
from .models import Booking, Contact
from django.contrib import messages
from django.core.mail import send_mail

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