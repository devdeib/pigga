from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.user.username


class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
      return self.name
   
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='menu_images/', blank=True, null=True)
