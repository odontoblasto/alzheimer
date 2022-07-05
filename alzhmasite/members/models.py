from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):


    name = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    data_nascimento= models.DateField(null=True)
    foto = models.ImageField(null=True,blank=True,upload_to='images/profile')
   

    def __str__(self):
        return str(self.name) 

    def get_absolute_url(self):
        return reverse('home')
