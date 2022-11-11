from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Help
from chat.models import Room
from account.models import Account

# Create your views here.


def aboutus(request):
    account = None
    if not User.is_anonymous :
        account = Account.objects.get(user=request.user)
    return render(request, 'Aboutus/aboutus.html', {'account': account, })


def help(request):
    account = None
    if not User.is_anonymous :
        account = Account.objects.get(user=request.user)
    return render(request, 'Aboutus/help.html', {'account': account, })


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
    return HttpResponseRedirect(reverse('home'))
    # return render(request, "registration/login.html", {
    #     "messages": messages.get_messages(request)
    # })


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


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out.")
    return HttpResponseRedirect(reverse('home'))


def home(request):
    account = None
    if not User.is_anonymous :
        account = Account.objects.get(user=request.user)
    
    text = ""
    if request.method == 'POST':
        text = request.POST.post('text')
    return render(request, "users/home.html", {
        "rooms": Room.objects.all(),
        "text": text,
        "account":account,
        
    })


def signup(request):
    return render(request, "registration/signup.html")


def help_send(request):

    report = request.GET.get('help_send')
    form = Help.objects.create(user=report)
    form.save()
    return HttpResponseRedirect('help')
