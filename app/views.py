from django.shortcuts import render,redirect
from . models import blog
from . forms import blog_form
from django.http import HttpResponse
from .forms import signupform

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.
# @login_required(login_url="login")
def Home(request):
    return render(request,"home.html")


def signup(request):
    if request.user.is_authenticated:
        return redirect(request,'Home')
    else:
        if request.method == 'POST':
            form = signupform(request.POST)
            if form.is_valid():
                form.save()

                messages.success(request,"Your account has been created")
                return redirect(loginUser)

        else:
            form = signupform()
        return render(request,'signup.html',{"form":form})


def loginUser(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        upass = request.POST.get('password')
        
        user = authenticate(request,username=uname,password=upass)

        if user is not None:
            login(request,user)
            return redirect(Home)
        else:
            messages.info(request,"Username OR Password is incorrect")
        
    return render (request,'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')
    
@login_required(login_url="login")
def Post(request):
    if request.method=="POST":
        form=blog_form(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(Read)
        
    else:
        form=blog_form()
    return render(request,"post.html",{"form":form})



@login_required(login_url="login")
def Read(request):
    read=blog.objects.all()
    return render(request,"read.html",{"read":read})

@login_required(login_url="login")
def Update(request,id):
    upd= blog.objects.get(id=id)
    update=blog_form(request.POST or None,request.FILES or None,instance=upd)
    if update.is_valid():
        update.save()
        return redirect(Read)
    return render(request,"update.html",{"update":update})


@login_required(login_url="login")
def Delete(request,id):
    del_t=blog.objects.get(id=id)
    del_t.delete()

    return redirect(Read)
    
    