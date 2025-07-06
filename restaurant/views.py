from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from django.core import serializers
from .models import Booking
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import views, viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import Menu, Booking
from .serializer import MenuSerializer, BookingSerializer, UserSerializer
from .permissions import IsAdmin, IsManager, IsCustomer, ReadOnly


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin | IsManager]
        return [permission() for permission in permission_classes]


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    def get_permissions(self):
        if self.request.method in ["GET","POST"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin | IsManager]
        return [permission() for permission in permission_classes]


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin]
    queryset = User.objects.all()
    serializer_class = UserSerializer            

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        booking = Booking(
            first_name=data['first_name'],
            reservation_date=data['reservation_date'],
            reservation_slot=data['reservation_slot']
        )
        booking.save()
        return JsonResponse({'status': 'created'})
    elif request.method == 'GET':
        date = request.GET.get('date')
        bookings = Booking.objects.filter(reservation_date=date)
        booking_json = serializers.serialize('json', bookings)
        return HttpResponse(booking_json, content_type='application/json')
