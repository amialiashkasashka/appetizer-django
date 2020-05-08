from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name    

class Blog(models.Model):
    title           = models.CharField(max_length=200)
    author          = models.CharField(max_length=200)
    photo_main      = models.ImageField(upload_to='photos/%Y/%m/%d/')
    list_date       = models.DateTimeField(default=datetime.now, blank=True)
    is_published    = models.BooleanField(default=True)
    header1_bs      = models.CharField(max_length=200, null=True, blank=True)
    text1_bs        = models.TextField(max_length=5000, null=True, blank=True)
    header2_bs      = models.CharField(max_length=200, null=True, blank=True)
    text2_bs        = models.TextField(max_length=5000, null=True, blank=True)
    photo_bs        = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    text3_bs        = models.TextField(max_length=5000, null=True, blank=True)
    photo_person_bs = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    name_person_bs  = models.CharField(max_length=200, null=True, blank=True)
    text_person_bs  = models.CharField(max_length=400, null=True, blank=True)
    tags            = models.ManyToManyField(Tag)
    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('blogsingle', kwargs={
            'id': self.id
        }) 

    @property
    def get_comments(self):
        return self.comments.all()    

class Comment(models.Model):
    blog        = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', null=True)
    user        = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    message     = models.TextField(blank=True, null=True)
    name        = models.CharField(max_length=200, null=True)
    email       = models.EmailField(null=True)
    created_on  = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name


        