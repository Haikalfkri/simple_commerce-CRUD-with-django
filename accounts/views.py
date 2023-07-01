from django.shortcuts import render, redirect
from accounts.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.info(request, "Login successfull")
            return redirect ('item:home')
        else:
            messages.error(request, 'Invalid username or password.')
            
    return render(request, "login.html")


def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Registration successfully")
            return redirect("account:login")
    else:
        form = CreateUserForm()
    return render(request, "signup.html", {'form':form})


@login_required
def user_logout(request):
    logout(request)
    return redirect("item:home")