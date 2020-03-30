from django.db import models

# Create your models here.
 
class Category(models.Model):
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.category


class Menu(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    food_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    is_on_home_page = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Chefs(models.Model):

    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name
   