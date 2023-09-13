from django.shortcuts import render
from django.contrib import messages
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
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass2')
        pass2=request.POST.get('pass2')
        print(fname,lname,email,pass1,pass2)

    return render(request,"signup.html")