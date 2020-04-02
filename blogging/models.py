from django.db import models
from datetime import datetime

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title