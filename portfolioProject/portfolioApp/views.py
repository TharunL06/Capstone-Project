from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def blog(request):
    return render(request,"blog.html")

def handlelogin(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")