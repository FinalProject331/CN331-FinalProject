
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
from chat.models import Message
from django.http import HttpResponse, JsonResponse

# let staff view the detail of shop
def myshop(request):
    
    user = request.user
    shop = Shop.objects.get(staff = user)

    return render(request, 'shop/myshop.html',{
        "shop" : shop,
        "user" : user
    })

# let staff modify the detail of shop
def modifyshop(request):

    shop = Shop.objects.get(staff = request.user)
    
    return render(request, 'shop/modifyshop.html',{
        "shop": shop    
    })

# modify actions 
def modify(request):
    name = request.GET.get('name')
    bio = request.GET.get('bio')

    user = request.user
    shop = Shop.objects.get(staff=user)

    shop.name = name
    shop.detail = bio

    shop.save()
    shop.refresh_from_db()
    # account.user = user
    # account.detail = bio
    # account.save()
    # account.refresh_from_db()
    return HttpResponseRedirect(reverse('myshop'))
    
    # # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     form = ShopForm(request.POST, instance=request.user.staff) 
    #     # check whether it's valid:
    #     if form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         form.save()
    #         messages.success(request, 'Your profile is updated successfully')
    #         return redirect(to='myshop')
    #     else:
    #         messages.error(request,('error ka'))
    # else:
    #     form = ShopForm(instance=request.user.staff)

    # return render(request, 'myshop.html', {'form': form})

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
    account = Account.objects.get(user=request.user)
    return render(request, 'shop/myshop.html', {
        'shop': shop,
        'account': account })

"""
chat with staff

"""

def shoproom(request, room):
    room_details = ShopChat.objects.get(name=room)
    user = request.user
    username = user.username
    account = None
    if not user.is_staff:
        account = Account.objects.get(user=user)
    return render(request, 'shop/shopchat.html', {
        'user': user,
        'username': username,
        'room': room,
        'room_details': room_details,
        'account': account
    })

def shopcheckview(request, shop):
    shopobj = Shop.objects.get(name = shop)
    staff = shopobj.staff
    # room = shop+str(request.user.id)
    user = request.user
    username = user.username
    room_name = shop+username

    if ShopChat.objects.filter(name=room_name).exists():
        return redirect('/shop/'+room_name+'/?username='+username)
    else:
        new_room = ShopChat.objects.create(name=room_name, staff = staff, customer = username, restaurant_name = shop)
        new_room.save()
        return redirect('/shop/'+room_name+'/?username='+username)

def shopsend(request):
    message = request.POST['message']
    username = request.POST['username']
    room_name = request.POST['room_name']

    new_message = Message.objects.create(value=message, user=username, room=room_name)
    new_message.save()
    return HttpResponse('Message sent successfully')

def shopgetMessages(request, room):
    room_details = ShopChat.objects.get(name=room)

    messages = Message.objects.filter(room=room)
    return JsonResponse({"messages":list(messages.values())})

def join_chat(request, chat):
    username = request.user.username
    
    return redirect('/shop/'+chat+'/?username='+username)

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
