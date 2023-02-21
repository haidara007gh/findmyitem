from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    
    def __str__(self):
        return f"Phone: {self.phone_number}, Email: {self.email}"
    
class Item(models.Model):
    # url = models.ImageField(upload_to="images/", null=True)
    url = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    location = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}:{self.category},{self.description},{self.location}"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="posted_by", related_name="posts")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="items")
    datetime = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=64) 
      #'found','missen','collectedbyowner'
    
    def __str__(self):
        return f"{self.user}:{self.item}\n{self.datetime},{self.type}"



