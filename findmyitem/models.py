from django.contrib.auth.models import AbstractUser
from django.db import models
from django_google_maps import fields as map_fields

# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.id}"
           
class Item(models.Model):
    R = "R"
    M = "M"
    F = "F"
    
    STATUS_CHOICES = [
        (R, "Report lost item"),    #Item reported by owner who needs notification when item found
        (M, "Missing Item"),        #Item posted by a volunteer who found it
        (F, "Found by owner")       #Item collected by owner
    ]
    
    name = models.CharField(max_length=64)
    img_url = models.ImageField(upload_to="images/", null=True)
    category = models.CharField(max_length=64)
    description = models.CharField(max_length=64)

    geolocation = map_fields.GeoLocationField(max_length=100)
    address = map_fields.AddressField(max_length = 200)
    place = models.CharField(max_length=64)
    
    is_taken = models.BooleanField(verbose_name="Action")
    status = models.CharField(choices=STATUS_CHOICES,max_length=1,default=M)
     
    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="related_post")
    
    posted_by= models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    posting_datetime = models.DateTimeField(auto_now=True)
    
    taken_by= models.ForeignKey(User, on_delete=models.CASCADE, related_name="responsible_for")
    taking_datetime = models.DateTimeField()
    
    def __str__(self):
        return f"{self.id},{self.item},{self.posted_by},{self.posting_datetime},{self.taken_by},{self.taking_datetime}"
    

