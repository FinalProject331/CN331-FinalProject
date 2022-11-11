
# from django.conf import settings
from django.shortcuts import render
# from django.templatetags.static import static
from account.models import Account
from shop.models import Shop, ShopChat
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from .forms import ShopForm
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

# let staff view the detail of shop
def myshop(request):
    
    user = request.user
    
    shop = Shop.objects.get_or_create(staff = user)

    return render(request, 'shop/myshop.html',{
        shop : "shop"
    })

# let staff modify the detail of shop
def modifyshop(request):

    shop = Shop.objects.get(staff = request.user)
    
    return render(request, 'shop/modifyshop.html',{
        shop : "shop"
    
    })

# modify actions 
def modify(request):
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ShopForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...



            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ShopForm()

    return render(request, 'name.html', {'form': form})

def upload(request):
    if request.method == 'POST':
        shop_form = ShopForm(request.POST, request.FILES, instance=request.user.profile)
        if shop_form.is_valid():            
            shop_form.save()
            messages.success(request, 'Your shop is updated successfully')
            return redirect(to='myshop')
        else:
            messages.error(request, ('error ka'))
    else:
        shop_form = ShopForm(instance=request.user.profile)

    return render(request, 'myshop.html', {
        'shop_form': shop_form
    })
    