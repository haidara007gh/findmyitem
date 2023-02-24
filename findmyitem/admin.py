from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone_number")

class ItemAdmin(admin.ModelAdmin):
    list_display = ("id","name","category","description","url","location")

class PostAdmin(admin.ModelAdmin):
    list_display = ("id","datetime", "type","item","user")

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Post, PostAdmin)