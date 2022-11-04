from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from chat.models import Room



from account.models import Account

# Create your views here.

def aboutus(request):
    return render(request, 'Aboutus/aboutus.html')
def help(request):
    return render(request, 'Aboutus/help.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('home'))
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




def home(request):
    
    return render(request,"users/home.html",{
        "Rooms": Room.objects.all()
    })

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    