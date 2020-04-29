from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name


        