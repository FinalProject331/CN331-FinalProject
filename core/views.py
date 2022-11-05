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
from .models import Help

from chat.models import Room
from .models import Help



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
        birthday = request.POST["birthday"]
        gender = request.POST["gender"]
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

def create_account(user, birthday, gender):
    account = Account.objects.create(user = user, birthday= birthday, gender = gender)
    account.save()
    account.refresh_from_db()
    return account

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out.")
    return render(request, "accounts/login.html", {
        "messages": messages.get_messages(request)
    })




def home(request):
    user = request.user
    # if user is not None:
    #     account = Account.objects.get(user = request.user)
    return render(request,"users/home.html",{
        "rooms": Room.objects.all(),
        # "account" : account
    })

<<<<<<< HEAD
def signup(request):
    username = request.POST["username"]
    password = request.POST["password"]
    birthday = request.POST["birthday"]
    gender = request.POST["gender"]
    user = User.objects.create_user(username = username, password= password)
    if request.method == 'POST':
        account = create_account(user, birthday,gender)
    return render(request, "accounts/login.html")
    
def help_send(request):
    report = "-"
    if request.method == 'POST':
        report = request.POST['help_send']
    form  = Help.objects.create(report = report)
    form.save()
    return render(request, "users/home.html")
    
=======
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
def help_send(request):
    
    report = request.GET.get('help_send')
    form = Help.objects.create(user = report)
    form.save()
    return HttpResponseRedirect('help')
>>>>>>> a3716ba150f3b146a81c52f0f349abc15051b890
