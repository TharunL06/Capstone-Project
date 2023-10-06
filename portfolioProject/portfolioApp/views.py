# redirect is used to redirecting the specific url
from django.shortcuts import render,redirect
from django.contrib import messages
# user is default database provided by django where we store the data
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Blog, Contact, Skill

# Create your views here.
def index(request):
    data=Skill.objects.all()
    context={"data":data}
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def contact(request):
    if not request.user.is_authenticated:
        messages.info(request,"Please Login to contact us")
        return render(request,"login.html")
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['num']
        desc=request.POST['desc']
        if len(phone)>10 or len(phone)<10:
            messages.warning(request,"Please enter the 10 digit number")
            return redirect("/contact")
        query=Contact(name=name,email=email,phone=phone,description=desc)
        query.save()
        messages.success(request,"Thanks for contacting us, we will get back you soon")
        return redirect("/contact")
        
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