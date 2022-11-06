# Create your views here.

from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from account.models import Account

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
    if this_room.id != account.chat and account.chat == 0 and this_room.is_seat_available():
        this_room.seat_count += 1
        account.chat = this_room.id
        this_room.save()
        account.save()
        return redirect('/'+room+'/?username='+username)
    elif this_room.id == account.chat:
        return redirect('/'+room+'/?username='+username)
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


def checkview(request):
    room = request.POST['room_name']
    username = request.user.username
    user = request.user
    account = Account.objects.get(user=user)
    if account.chat != 0:
        messages.warning(
            request, "leave the previous room before create new room.")
        return render(request, 'chat/roomconfig.html')
    elif Room.objects.filter(name=room).exists():
        return render(request, 'chat/roomdetail.html', {
            "messages": messages.get_messages(request),
            'room': Room.objects.get(name=room)
        })
    else:
        new_room = Room.objects.create(name=room)
        account.chat = new_room.id
        account.save()
        new_room.save()
        return redirect('/'+room+'/?username='+username)


def create_room(request):
    room_name = request.POST['room_name']
    room = Room.objects.create(name=room_name)

    return redirect('/'+room_name+'/?username='+request.user.username)


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
    return render(request, 'chat/roomdetail.html', {
        'room': Room.objects.get(name=room),
        'account':account,
        })


def return_chat(request, chat):
    username = request.user.username
    this_room = Room.objects.get(id=chat)
    return redirect('/'+this_room.name+'/?username='+username)
