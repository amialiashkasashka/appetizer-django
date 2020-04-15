from django.db import models

# Create your models here.
 
class Category(models.Model):
    category = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.category


class Menu(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=True)
    food_image = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    is_published = models.BooleanField(default=True, null=True)
    is_on_home_page = models.BooleanField(default=False, null=True)
    def __str__(self):
        return self.name

class Chefs(models.Model):

    name = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    description = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name
   