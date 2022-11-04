from django.shortcuts import render
from .models import Account
# Create your views here.

def myprofile(request):
    account = Account.objects.get_or_create(user = request.user)
    
    return render(request, 'account/myprofile.html',{
        "account" : account
    
    })

def editprofile(request):
    return render(request, 'account/editprofile.html')
