from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=200, blank=True)
    guests = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    header = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.header