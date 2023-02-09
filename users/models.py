from distutils.command.upload import upload


from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField

# Create your models here.

# one to one relation meaning one user have one profile
class Profile(models.Model):
# inorder to associated user
    user = models.OneToOneField(User, on_delete = models.CASCADE) # this means if u delete your account , its going to delete your Profile aswell
    # now we can add our very own fields over here
    
    image = models.ImageField(default= 'profilepic.jpg', upload_to= 'profile_pics')
    location = models.CharField( max_length=150)    
    
    def __str__(self):
        return self.user.username

