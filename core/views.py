from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Help

from chat.models import Room
from .models import Help


from account.models import Account

# Create your views here.


def aboutus(request):
    return render(request, 'Aboutus/aboutus.html')


def help(request):
    return render(request, 'Aboutus/help.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return HttpResponseRedirect(reverse('home'))
        else:
            messages.warning(request, "Invalid credential.")
            return render(request, "registration/login.html", {
                "messages": messages.get_messages(request)
            })

    return render(request, "registration/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out.")
    return render(request, "registration/login.html", {
        "messages": messages.get_messages(request)
    })

def create_account(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    username = request.GET.get('username')
    password = request.GET.get('password')
    birthday = request.GET.get('birthday')
    gender = request.GET.get('gender')

    user = User.objects.create(username=username,
                               first_name=first_name, last_name=last_name, email=email)
    user.is_active = True
    user.set_password(password)
    user.save()
    user.refresh_from_db()
    account = Account.objects.create(
        user=user, birthday=birthday, gender=gender)
    account.save()
    account.refresh_from_db()
    return HttpResponseRedirect(reverse('login'))




def home(request):
    text = ""
    if request.method == 'POST':

        text = request.POST.post('text')
    return render(request, "users/home.html", {
        "rooms": Room.objects.all(),
        "text": text
    })


def signup(request):

    return render(request, "registration/signup.html")


def help_send(request):

    report = request.GET.get('help_send')
    form = Help.objects.create(user=report)
    form.save()
    return HttpResponseRedirect('help')
