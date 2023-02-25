from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("post/", views.post, name="post"),
    path("post/submit/", views.pSubmit, name="pSubmit"),
    path("post/submit/message/", views.pMessage, name="pMessage"),
    
    path("search/", views.search, name="search"),
]