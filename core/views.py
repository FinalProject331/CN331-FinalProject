from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Help
from chat.models import Room
from account.models import Account
from shop.models import ShopChat, Shop
from chat.views import check_gender, cal_age
# Create your views here.


def aboutus(request):
    if request.user.is_anonymous or request.user.is_staff:
        account = None
    else:
        account = Account.objects.get(user=request.user)
    return render(request, 'Aboutus/aboutus.html', {'account': account, })


def help(request):
    if request.user.is_anonymous or request.user.is_staff:
        account = None
    else:
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


def create_account(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    repeat_password = request.POST.get('repeat_password')
    birthday = request.POST.get('birthday')
    gender = request.POST.get('gender')

    if password != repeat_password:
        messages.error(request, "Password and Repeat Password didn't match")
        return HttpResponseRedirect(reverse("signup"))

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
    age = cal_age(account.birthday)
    account.age = age
    account.save()
    return HttpResponseRedirect(reverse('login'))


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out.")
    return HttpResponseRedirect(reverse('home'))


def home(request):
    user = request.user

    # staff site
    if user.is_staff and (not user.is_superuser):
        shop = Shop.objects.get(staff=user)
        chats = ShopChat.objects.all().filter(staff=user.username)
        return render(request, "users/home.html", {
            "chats": chats,
            "shop": shop,
        })

    # anonymous site and admin site
    if user.is_anonymous or user.is_superuser:
        account = None
    else:
        account = Account.objects.get(user=user)

    # user site
    return render(request, "users/home.html", {
        "rooms": Room.objects.all(),
        "account": account,
        "filter": "Filter"
    })


def signup(request):
    return render(request, "registration/signup.html")


def help_send(request):

    report = request.GET.get('help_send')
    form = Help.objects.create(user=report)
    form.save()
    return HttpResponseRedirect('help')


def search(request):
    account = Account.objects.get(user=request.user)
    text = request.GET['search']
    all_room = Room.objects.all()
    rooms = []
    if text != "":
        for room in all_room:
            if text in room.name:
                rooms.append(room)
        if rooms == []:
            messages.warning(
                request, "Room name '"+text+"' does not exist.")
            return HttpResponseRedirect(reverse('home'))
        return render(request, "users/home.html", {
            "rooms": rooms,
            "account": account,
        })
    else:
        return HttpResponseRedirect(reverse('home'))

def filter(request):
    account = Account.objects.get(user=request.user)
    filter = request.POST['filter']
    all_room = Room.objects.all()
    rooms = []
    if filter == "All":
        rooms = all_room
    else:
        for room in all_room:
            if filter in room.filter:
                rooms.append(room)
    return render(request, "users/home.html", {
        "rooms": rooms,
        "filter": filter,
        "account": account,
    })

def joinable(request):
    checked = request.GET.get('checked', False)
    all_room = Room.objects.all()
    rooms = []
    account = Account.objects.get(user=request.user)
    if checked:
        is_checked = True
        for room in all_room:
            if room.is_available and check_gender(room.request_gender, account.gender):
                rooms.append(room)
    else:
        rooms = all_room
        is_checked = False
    return render(request, "users/home.html", {
        "rooms": rooms,
        "is_checked": is_checked,
        "filter": "Filter",
        "account": account,
    })