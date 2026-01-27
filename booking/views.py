from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def create_booking(request, property_id):
    # Logic to create a booking for a specific property
    context = {
        'property_id': property_id,
        'user': request.user
    }
    return render(request, 'booking/create_booking.html', {'context': context})


@login_required()
def booking_detail(request, booking_id):
    # Logic to retrieve and display details of a specific booking
    return render(request, 'booking/booking_detail.html', {'booking_id': booking_id})
