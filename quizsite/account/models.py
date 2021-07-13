from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    GENDER_CHOICES = (
        ('M', 'Male',),
        ('F', 'Female',),
        ('U', 'Others',),
    )
    gender=models.CharField( max_length = 20,choices=GENDER_CHOICES,default="")
    contact_no=models.IntegerField(blank=True,null=True)
    city = models.CharField(max_length=100,default="",blank=True)
    country = models.CharField(max_length=100,default="",blank=True)
    profile_image=models.ImageField(default='default.png',upload_to='profile_pic',blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
