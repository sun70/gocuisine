from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from GoCuisineApp.models import hotel_details_table


def index(request):
    return render(request,'index.html')


def displayhotel(request):
    message = 'You have searched the location which is yet to explore for us....Thanks'
    if 'address' in request.POST:
        address = request.POST['address']
        hotel = hotel_details_table.objects.filter(hotel_address__icontains=address)
        hotel_count = hotel.count()
        if hotel_count==0:
            return render(request,'error404.html',{'message':message})
        else:
            hotel = hotel_details_table.objects.filter(hotel_address__icontains=address)
            return render(request, 'hotels.html', {'hotel':hotel , 'hotel_count':hotel_count , 'address':address})
    else:
        return render(request,'error404.html',{'message':message})


def reservationpage(request):
    hotel_id = request.POST['hotel_id']
    int(hotel_id)
    hotel_detail = hotel_details_table.objects.filter(id = hotel_id)
    address = request.POST['address']
    hotel_count = hotel_detail.count()
    return render(request, 'reservation_page.html', {'hotel':hotel_detail,'hotel_count':hotel_count, 'address':address})

def redirect_to_login(request):
    return render(request,'login.html')

def login_handler(request):
    if 'username' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username,password)
        if user.is_authenticated is None:
            return render(request,'login.html')
        else:
            return render(request, 'reservation_page.html')
    else:
        return render(request,'login.html')



@login_required()
def cab_handler(request):
    return render(request,'book_cab.html')

def register_handler(request):
    return render(request,'register.html')


def bookcab(request):
    return render(request,'successful.html')

