from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from booking.forms import CreateBookingForm
from booking.models import Booking

# Create your views here.


@login_required()
def create_booking(request, property_id):
    if request.method == 'POST':
        form = CreateBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.created_by = request.user
            # You may want to set property_id to booking if your model supports it
            # booking.property_id = property_id
            booking.save()
            messages.success(request, 'Booking created successfully!')
            return redirect('booking:booking_detail', booking_id=booking.id)
    else:
        form = CreateBookingForm()

    context = {
        'form': form,
        'property_id': property_id,
        'user': request.user
    }
    return render(request, 'booking/create_booking.html', context)


@login_required()
def booking_detail(request, booking_id):
    # Logic to retrieve and display details of a specific booking
    return render(request, 'booking/booking_detail.html', {'booking_id': booking_id})
