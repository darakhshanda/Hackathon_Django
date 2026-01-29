from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from requests import request
import booking
from property.models import Property
from booking.forms import CreateBookingForm, UpdateBookingForm
from booking.models import Booking


@login_required()
def create_booking(request, property_id):
    """Create a booking for a specific property"""

    # Get the property
    property_obj = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        form = CreateBookingForm(request.POST)

        if form.is_valid():
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            guests = form.cleaned_data['guests']

            # Check if property is available using our new method
            if property_obj.is_available(check_in, check_out):
                # Create the booking as PENDING (admin needs to confirm)
                booking = form.save(commit=False)
                booking.user = request.user
                booking.property = property_obj

                # Calculate total price
                nights = (check_out - check_in).days
                booking.total_price = property_obj.price_per_night * nights
                booking.status = 'pending'  # Starts as pending

                booking.save()

                messages.success(
                    request,
                    "Booking request submitted! It will be confirmed by our team."
                )
                return redirect('booking:booking_detail', booking_id=booking.id)
            else:
                messages.error(
                    request,
                    "Sorry, this property is not available for the selected dates."
                )
    else:
        form = CreateBookingForm()

    context = {
        'form': form,
        'property': property_obj,
    }
    return render(request, 'booking/create_booking.html', context)


@login_required()
def booking_detail(request, booking_id):
    """Show booking details"""
    booking = get_object_or_404(Booking, id=booking_id)

    # Only show booking to the user who created it
    if booking.user != request.user:
        messages.error(request, "You can only view your own bookings.")
        return redirect('index_url')

    return render(request, 'booking/booking_detail.html', {'booking': booking})


@login_required()
def cancel_booking(request, booking_id):
    """Cancel a booking"""
    booking = get_object_or_404(Booking, id=booking_id)

    # Security check: Only the booking owner can cancel
    if booking.user != request.user:
        messages.error(request, "You can only cancel your own bookings.")
        return redirect('index_url')

    # Only allow cancellation of pending or confirmed bookings
    if booking.status not in ['pending', 'confirmed']:
        messages.error(request, f"Cannot cancel a {booking.status} booking.")
        return redirect('booking:booking_detail', booking_id=booking.id)

    if request.method == 'POST':
        # Confirm cancellation
        booking.status = 'cancelled'
        booking.save()

        messages.success(
            request,
            f"Booking for {booking.property.name} has been cancelled successfully."
        )
        return redirect('user_profile', user_id=request.user.id)

    # Show confirmation page
    context = {
        'booking': booking,
    }
    return render(request, 'booking/cancel_booking.html', context)


@login_required()
def edit_booking(request, booking_id):
    """Edit an existing booking"""
    booking = get_object_or_404(Booking, id=booking_id)

    # Security check: Only the booking owner can edit
    if booking.user != request.user:
        messages.error(request, "You can only edit your own bookings.")
        return redirect('index_url')

    # Only allow editing of pending bookings
    if booking.status == 'completed':
        messages.error(request, f"Cannot edit a completed booking.")
        return redirect('booking:booking_detail', booking_id=booking.id)
    elif booking.status == 'cancelled':
        messages.error(request, "Cannot edit a cancelled booking.")
        return redirect('booking:booking_detail', booking_id=booking.id)

    if request.method == 'POST':
        form = UpdateBookingForm(request.POST, instance=booking)

        if form.is_valid():
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']

            # Check if property is available for new dates
            if booking.property.is_available(check_in, check_out, exclude_booking_id=booking.id):
                updated_booking = form.save(commit=False)

                # Recalculate total price
                nights = (check_out - check_in).days
                updated_booking.total_price = booking.property.price_per_night * nights

                updated_booking.save()

                messages.success(
                    request,
                    "Booking updated successfully!"
                )
                return redirect('booking:booking_detail', booking_id=booking.id)
            else:
                messages.error(
                    request,
                    "Sorry, this property is not available for the selected dates."
                )
    else:
        form = UpdateBookingForm(instance=booking)

    context = {
        'form': form,
        'booking': booking,
        'property': booking.property,
    }
    return render(request, 'booking/edit_booking.html', context)
