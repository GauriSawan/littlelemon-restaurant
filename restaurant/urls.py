from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('bookings/', views.bookings, name='bookings'),
    path('api-token-auth/', obtain_auth_token),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),

]