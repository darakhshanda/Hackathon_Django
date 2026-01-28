
from django import views
from django.urls import path
from . import views


app_name = 'booking'

urlpatterns = [
    path('book/<int:property_id>/', views.create_booking, name='create_booking'),
    path('booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),
]
