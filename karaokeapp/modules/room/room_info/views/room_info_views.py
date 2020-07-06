from django.shortcuts import render
from karaokeapp.modules.room.room_info.forms.room_info_forms import RoomForm
from karaokeapp.modules.room.room_info.models.room_info_models import Room
from django.shortcuts import render, redirect , render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from django.core.paginator import InvalidPage, Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
@login_required
def listRoomInfo(request):
    if request.method == 'POST':
        return render(request, 'room/list_room_info.html')
    else:   
        roomInfo = Room.objects.all().order_by('id');
        paginator = Paginator(roomInfo, 3)
        page = request.GET.get('page', 1)
        try:
            listRoom = paginator.page(page)
        except PageNotAnInteger:
            listRoom = paginator.page(1)
        except EmptyPage:
            listRoom = paginator.page(paginator.num_pages)
        return render(request, 'room/list_room_info.html', {'listRoom':listRoom})
@login_required
def addRoomInfo(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            room_name = data['name']
            room_status = data['status']
            note = data['note']
            user = Room.objects.create(name= room_name, status= room_status, note = note,)
    roomInfo = Room.objects.all().order_by('id');
    paginator = Paginator(roomInfo, 3)
    page = request.GET.get('page', 1)
    try:
        listRoom = paginator.page(page)
    except PageNotAnInteger:
        listRoom = paginator.page(1)
    except EmptyPage:
        listRoom = paginator.page(paginator.num_pages)
    return render(request, 'room/list_room_info.html', {'listRoom':listRoom})
def getRoom(request):
    if request.method == 'GET':
        tabType = request.GET.get('tabType')
        if tabType == 'aaaaa':
            roomInfo = Room.objects.filter(status=1)
            paginator = Paginator(roomInfo, 3)
            page = request.GET.get('page', 1)
            try:
                listRoom = paginator.page(page)
            except PageNotAnInteger:
                listRoom = paginator.page(1)
            except EmptyPage:
                listRoom = paginator.page(paginator.num_pages)
            return JsonResponse({ 'listRoom' : listRoom,})
    else:
        return render(request, 'room/list_room_info.html', {'listRoom':listRoom}) 