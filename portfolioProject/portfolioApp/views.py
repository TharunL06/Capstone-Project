# redirect is used to redirecting the specific url
from django.shortcuts import render,redirect
from django.contrib import messages
# user is default database provided by django where we store the data
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Blog

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def blog(request):
    data=Blog.objects.all()
    # print(data)
    context={"data":data}
    return render(request,"blog.html",context)

def handlelogin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        user=authenticate(username=email,password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request,"Login sucessful")
            return redirect('/')
        else :
            messages.error(request,"Invalid credentials, Try again")
            return redirect('/login')


    return render(request,"login.html")

def signup(request):
    if request.method=="POST":
        # this line are used to pass the data from frontend to backend
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        # validate password and confirm password
        if pass2!=pass1:
            messages.warning(request,"Password is not matching")
            return redirect('/signup')
        # print(fname,lname,email,pass1,pass2)
        # i am validating the user exits or not with the same email and username
        

        try:
            if User.objects.get(username=email):
                messages.warning(request,"User Already Exist")  
                return redirect('/signup')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request,"email Already Exist")
                return redirect('/signup')
        except:
            pass
        # using email as username also, for that gave 2 email arg
        user=User.objects.create_user(email,email,pass1)
        user.first_name=fname
        user.last_name=lname
        user.save()
        # this line display the message when user signuo successfuly
        messages.success(request,"Signup Success")
        return redirect('/login')
        # this line display message over the signup section
        # messages.info(request,f'{fname},{lname},{email},{pass1},{pass2}')


    return render(request,"signup.html")

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout succesful")
    return redirect('/login')