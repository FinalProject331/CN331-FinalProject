from django.conf import settings
from django.shortcuts import render , redirect
from django.templatetags.static import static
from .models import Account
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
# Create your views here.

def myprofile(request):
    
    user = request.user
    account = Account.objects.get(user = user)
    return render(request, 'account/myprofile.html',{
        "account" : account,
    })

def editprofile(request):
    account = Account.objects.get(user = request.user)
    
    return render(request, 'account/editprofile.html',{
        "account" : account
    
    })

def edit(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    bio = request.GET.get('bio')
    username = request.GET.get('username')
    
    
    user = request.user
    account = Account.objects.get(user=user)

    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.username = username
    
    user.save()
    user.refresh_from_db()
    account.user = user
    account.bio = bio
    account.save()
    account.refresh_from_db()
    return HttpResponseRedirect(reverse('myprofile'))

from django.core.files.storage import FileSystemStorage

def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'editprofile', {'file_url': file_url})
    return render(request, 'editprofile')
