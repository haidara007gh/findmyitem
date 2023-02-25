from django.contrib import admin
from .models import *
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone_number")
    fields = ("email", "phone_number")

class ItemAdmin(admin.ModelAdmin):
    list_display = ("id","name","category","description","img_url","address","geolocation","place","status","is_taken")
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    } 

class PostAdmin(admin.ModelAdmin):
    list_display = ("id","posted_by","posting_datetime","taken_by","taking_datetime","item")

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Post, PostAdmin)