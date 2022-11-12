from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from account.models import Account
from chat.models import Message, Room
from datetime import datetime

# Create your views here.

def roomconfig(request):
    user = request.user
    account = Account.objects.get(user=user)

    return render(request, 'chat/roomconfig.html', {
        'account': account,
    })

def room(request, room):
    user = request.user
    account = Account.objects.get(user=user)

    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'chat/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details,
        'account': account
    })

def join_room(request, room):
    username = request.user.username
    this_room = Room.objects.get(name=room)
    account = Account.objects.get(user=request.user)
    if this_room.id != account.chat and account.chat == 0 and this_room.is_available() and check_gender(this_room.request_gender, account.gender):
        this_room.seat_count += 1
        account.chat = this_room.id
        this_room.save()
        account.save()
        return redirect('/'+room+'/?username='+username)
    elif this_room.id == account.chat:
        return redirect('/'+room+'/?username='+username)
    elif check_gender(this_room.request_gender, account.gender) == False:
        messages.warning(
            request, "Your gender is not match.")
        return render(request, 'chat/roomdetail.html', {
            "messages": messages.get_messages(request),
            'room': this_room,
            'account': account,
        })
    elif account.chat != 0:
        messages.warning(
            request, "leave the previous room before join new room.")
        return render(request, 'chat/roomdetail.html', {
            "messages": messages.get_messages(request),
            'room': this_room,
            'account': account,
        })
    else:
        messages.warning(request, "seat is not available.")
        return render(request, 'chat/roomdetail.html', {
            "messages": messages.get_messages(request),
            'room': this_room
        })

def check_gender(require, gender):
    if require == 'F' and gender != 'F':
        return False
    elif require == 'M' and gender != 'M':
        return False
    else:
        return True


def checkview(request):
    room = request.POST['room_name']
    max_seat = request.POST['max_seat']
    gender_request = request.POST['gender_request']
    dead_time = request.POST['dead_time']
    meal_time = request.POST['meal_time']

    username = request.user.username
    user = request.user
    account = Account.objects.get(user=user)
    if account.chat != 0:
        messages.warning(
            request, "leave the previous room before create new room.")
        return render(request, 'chat/roomconfig.html')
    # elif Room.objects.filter(name=room).exists():
    #     return render(request, 'chat/roomdetail.html', {
    #         "messages": messages.get_messages(request),
    #         'room': Room.objects.get(name=room)
    #     })
    elif (checkTime(dead_time) and checkTime(meal_time)):
        new_room = Room.objects.create(name=room)
        new_room.max_seat = max_seat
        new_room.request_gender = gender_request
        new_room.dead_time = dead_time
        new_room.meal_time = meal_time
        new_room.save()
        account.chat = new_room.id
        account.save()
        return redirect('/'+room+'/?username='+username)

    else:
        messages.warning(request, "Time not correct.")
        return render(request, 'chat/roomconfig.html')

# def create_room(request):
#     room_name = request.POST['room_name']
#     room = Room.objects.create(name=room_name)

#     return redirect('/'+room_name+'/?username='+request.user.username)

def checkTime(time):
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%dT%H:%M")
    if(time < date_time):
        return False
    else:
        return True

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(
        value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})

def room_detail(request, room):
    account = Account.objects.get(user=request.user)
    return render(request, "chat/roomdetail.html", {
        "room": Room.objects.get(name=room),
        "account": account,
        })

def return_chat(request, chat):
    username = request.user.username
    this_room = Room.objects.get(id=chat)
    return redirect('/'+this_room.name+'/?username='+username)

def leave_room(request, room):
    user = request.user
    account = Account.objects.get(user=user)
    account.chat = 0
    account.save()
    this_room = Room.objects.get(name=room)
    this_room.seat_count -= 1
    this_room.save()
    if this_room.seat_count == 0:
        this_room.delete()
    return redirect('home')

def edit_details(request, room):
    this_room = Room.objects.get(name=room)
    this_room.name = request.POST['room_name']
    this_room.max_seat = request.POST['max_seat']
    this_room.request_gender = request.POST['gender_request']
    this_room.dead_time = request.POST['dead_time']
    this_room.meal_time = request.POST['meal_time']
    this_room.status = request.POST['status']
    this_room.save()
    username = request.user.username
    return redirect('/'+this_room.name+'/?username='+username)

def edit_room(request, room):
    this_room = Room.objects.get(name=room)
    account = Account.objects.get(user=request.user)
    return render(request, 'chat/edit_room.html',{
        "room" : this_room,
        "account" : account,
    })