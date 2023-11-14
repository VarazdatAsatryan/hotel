from django.shortcuts import render,get_object_or_404,redirect
from .models import Booking,Room,Hotel
import datetime

def registration_list(request):
    booking = Booking.objects.all()
    return render(request,'polls/registration_list.html',{'booking':booking})

def registration_details(request,pk):
    bookings = get_object_or_404(Booking,pk = pk)
    return render(request,'polls/registration_details.html',{'bookings':bookings})


def add_room(request):
    room = Room.objects.all()
    hotel = Hotel.objects.all()
    if request.method == 'POST':

        name = request.POST.get('name')
        surename = request.POST.get('surename')
        number = request.POST.get('number')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        # check_in = datetime.strptime(check_in_str,'%Y-%m-%dT%H:%M')
        # check_out = datetime.strptime(check_out_str,'%Y-%m-%dT%H:%M')
        room_type = request.POST.get('room_type')
        hotels = request.POST.get('hotels')

        booking = Booking(
            name = name,
            surename = surename,
            number = number,
            check_in = check_in,
            check_out = check_out,
            room_type = room_type,
            hotels = hotels
        )
        booking.save()

        return redirect('polls:registration_list')

    return render(request,'polls/add_room.html',{'room':room,'hotel':hotel})




        
