
# from django.conf import settings
from django.shortcuts import render
# from django.templatetags.static import static
from account.models import Account
from shop.models import Shop, ShopChat, AddShop
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from .forms import ShopForm
from django.contrib import messages
from django.shortcuts import redirect
from chat.models import Message
from django.http import HttpResponse, JsonResponse

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
    
    shops = Shop.objects.all()

    return render(request, 'shop/shoplist.html',{
        "shops" : shops
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

"""
chat with staff

"""

def shoproom(request, room):
    username = request.user.username
    room_details = ShopChat.objects.get(name=room)
    return render(request, 'shop/shopchat.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def shopcheckview(request, shop):
    shopobj = Shop.objects.get(name = shop)
    staff = shopobj.staff
    room = shop+str(request.user.id)
    user = request.user
    username = user.username

    if ShopChat.objects.filter(name=room).exists():
        return redirect('/shop/'+room+'/?username='+username)
    else:
        new_room = ShopChat.objects.create(name=room, staff = staff, customer = username, restaurant_name = shop)
        new_room.save()
        return redirect('/shop/'+room+'/?username='+username)

def shopsend(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def shopgetMessages(request, room):
    room_details = ShopChat.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def join_chat(request, shop):
    username = request.user.username
    
    return redirect('/shop/'+shop+'/?username='+username)
