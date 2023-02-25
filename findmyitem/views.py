from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "homePage.html")

def post(request):
    return render(request, "post_start.html")

def search(request):
    return render(request, "search_start.html")