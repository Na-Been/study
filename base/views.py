from django.shortcuts import render, redirect
from .forms import RoomForm
from .models import Room

def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms': rooms})

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