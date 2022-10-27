from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.

def aboutus(request):
    return render(request, 'Aboutus/aboutus.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('users:index'))
        else:
            messages.warning(request, "Invalid credential.")
            return render(request, "accounts/login.html", {
                "messages": messages.get_messages(request)
            })

    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out.")
    return render(request, "accounts/login.html", {
        "messages": messages.get_messages(request)
    })

def signup(request):
    return render(request, "accounts/signup.html")

def create_user(request, email,name, password, birthday):
    user = User.objects.create_user(name, email, password)
    return render(request, "accounts/login.html")