from django.db import models


from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=50)
    item_price = models.IntegerField()
    item_image = models.CharField(default="https://cdn.dribbble.com/users/1012566/screenshots/4187820/media/985748436085f06bb2bd63686ff491a5.jpg?compress=1&resize=400x300&vertical=top" , max_length=1000)
    

    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self): # this wil redirect to detail page , i think its only work for CBV
        return reverse("food:detail", kwargs={"pk": self.pk})
    
