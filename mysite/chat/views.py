from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    print(request)
    return HttpResponse('not support to register')


@login_required
def index(request):
    print(request.user)
    return render(request, "chat/index.html")


@login_required
def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

