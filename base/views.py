from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import RoomForm
from .models import Room, Topic

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))
    #rooms = Room.objects.filter(topic__name=q).query
    #print(rooms.sql_with_params())
    topics = Topic.objects.all()
    return render(request, 'base/home.html', {'rooms': rooms,'topics': topics, 'room_count': rooms.count()})

def room(request,pk):
    room = Room.objects.get()
    return render(request, 'base/room.html')

def roomForm(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = RoomForm()
    return render(request, 'base/room_form.html', {'form': form})

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/room_form.html', {'form': form})

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html',{'obj': room})