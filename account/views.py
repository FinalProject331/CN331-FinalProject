from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static
from .models import Account
from django.http import HttpResponseRedirect
from django.urls import reverse
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

from .forms import ImageForm

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'account/editprofile', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'account/editprofile', {'form': form})