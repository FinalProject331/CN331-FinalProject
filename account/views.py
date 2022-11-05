from django.shortcuts import render
from .models import Account
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def myprofile(request):
    account = Account.objects.get(user = request.user)
    
    return render(request, 'account/myprofile.html',{
        "account" : account
    
    })

def editprofile(request):
    return render(request, 'account/editprofile.html')

def edit(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    bio = request.GET.get('bio')
    # username = request.GET.get('username')
    # password = request.GET.get('password')
    
    user = request.user
    account = Account.objects.get(user=user)

    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    # user.username = username
    # user.password = password
    user.save()
    user.refresh_from_db()
    account.user = user
    account.bio = bio
    account.save()
    account.refresh_from_db()
    return HttpResponseRedirect(reverse('myprofile'))