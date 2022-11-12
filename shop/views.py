
# from django.conf import settings
from django.shortcuts import render
# from django.templatetags.static import static
from account.models import Account
from shop.models import Shop, ShopChat, AddShop
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from .forms import ShopForm,ProfileShopForm
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

# let staff view the detail of shop
def myshop(request):
    
    user = request.user
    
    shop = Shop.objects.get_or_create(staff = user)

    return render(request, 'shop/myshop.html',{
        "shop" : shop
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

def uploadshop(request):
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
    
# view shop list
def shoplist(request):
    account = Account.objects.get(user=request.user)
    shops = Shop.objects.all()

    return render(request, 'shop/shoplist.html',{
        "shops" : shops,
        "account" : account
    })
    
# search shop
def search_shop(request):
    text = request.GET['search_shop']
    all_shop = Shop.objects.all()
    shops = []
    if text != "":
        for shop in all_shop:
            if text in shop.name :
                shops.append(shop)
        if shops == []:
            messages.warning(
                request, "Shop name '"+text+"' does not exist.")
            return HttpResponseRedirect(reverse('shoplist'))
        return render(request, "shop/shoplist.html", {
            "shops": shops,
    })
    else:
        return HttpResponseRedirect(reverse('shoplist'))

# add shop by name
def add_shop(request):
    account = Account.objects.get(user=request.user)
    return render(request, 'shop/addshop.html', {
        'account': account, })

# send 
def add_shop_send(request):
    report = request.GET.get('add_shop_send')
    form = AddShop.objects.create(user=report)
    form.save()
    return HttpResponseRedirect('add_shop')

# view the shop detail
def viewshop(request, id):
    shop = Shop.objects.get(pk=id)
    return render(request, 'shop/myshop.html', {
        'shop': shop, })





def shopupload(request):
    if request.method == 'POST':
        profile_form = ProfileShopForm(request.POST, request.FILES, instance=request.user.staff)
        if profile_form.is_valid():            
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='myshop')
        else:
            messages.error(request, ('error ka'))
    else:
        profile_form = ProfileShopForm(instance=request.user.staff)

    return render(request, 'myshop.html', {
        'profile_form': profile_form
    })