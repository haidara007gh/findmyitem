from django.shortcuts import render

def index(request):
    return render(request, "A_common/HomePage.html")

#--------------------------------------------

def post(request):
    return render(request, "B_post/1_start.html")

def pSubmit(request):
    return render(request, "B_post/2_submitting.html")

def pMessage(request):
    return render(request, "B_post/3_final_message.html")

#--------------------------------------------

def search(request):
    return render(request, "C_search/q.html")

