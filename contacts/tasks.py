from celery import shared_task
from time import sleep
from django.core.mail import send_mail

@shared_task
def send_mail_task(message):
    sleep(5)  

    return None
