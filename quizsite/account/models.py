from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, User
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    GENDER_CHOICES = (
        ('Male', 'Male',),
        ('Female', 'Female',),
        ('Others', 'Others',),
    )
    gender=models.CharField( max_length = 20,choices=GENDER_CHOICES,default="")
    contact_no=models.IntegerField(blank=True,null=True)
    city = models.CharField(max_length=100,default="",blank=True)
    country = models.CharField(max_length=100,default="",blank=True)
    desc=models.CharField(max_length=250,blank=True,default='',)
    profile_image=models.ImageField(upload_to='profile_pic',blank=True, null=True,default='default.png')

    def __str__(self):

        return f"{self.user.username} Profile"
