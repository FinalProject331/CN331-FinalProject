# from django.conf import settings
from tkinter import Image
from django.shortcuts import render
# from django.templatetags.static import static
from .models import Account
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from .forms import ProfileForm
from django.contrib import messages
from django.shortcuts import redirect
from PIL import Image

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



def upload(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='myprofile')
    else:
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'account/myprofile.html', {
        'profile_form': profile_form
    })