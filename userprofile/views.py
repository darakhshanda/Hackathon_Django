from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileSetupForm
from .models import UserProfile
from booking.models import Booking

# Create your views here.
# Profile Setup


def index(request):
    from property.models import Property
    properties = Property.objects.all()
    return render(request, 'index.html', {'properties': properties})


@login_required()
def profile_setup(request):
    if request.method == 'POST':
        form = ProfileSetupForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('index_url')
    else:
        form = ProfileSetupForm()
    return render(request, 'userprofile/profile_setup.html', {'form': form})


@login_required()
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileSetupForm(
            request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('index_url')
    else:
        form = ProfileSetupForm(instance=request.user.userprofile)
    return render(request, 'userprofile/profile_edit.html', {'form': form})


@login_required()
def user_profile(request, user_id):
    from django.contrib.auth.models import User
    from django.db.models import Count
    from django.shortcuts import get_object_or_404
    
    user = get_object_or_404(User, id=user_id)
    
    # SECURITY CHECK: Only allow users to view their own profile OR admins to view any profile
    if request.user.id != int(user_id) and not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, "You can only view your own profile.")
        return redirect('index_url')
    
    # Get user's bookings
    user_bookings = Booking.objects.filter(user=user).order_by('-created_at')
    
    # Calculate booking statistics (OPTIONAL PART)
    booking_stats = user_bookings.values('status').annotate(count=Count('status'))
    stats_dict = {stat['status']: stat['count'] for stat in booking_stats}
    
    # Get user profile (create one if it doesn't exist)
    try:
        user_profile = user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(
            user=user,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email
        )
    
    is_admin = request.user.is_staff or request.user.is_superuser
    
    return render(request, 'userprofile/userprofile.html', {
        'user_profiles': user_profile,
        'user_bookings': user_bookings,
        'booking_stats': stats_dict,
        'is_admin': is_admin,
    })

@login_required()
def delete_profile(request, user_id):
    user = request.user
    user.delete()
    return redirect('index')


@login_required()
def user_profiles_list(request):
    from django.contrib.auth.models import User
    users = User.objects.all()
    return render(request, 'userprofile/user_profiles_list.html', {'users': users})

@login_required()
def my_profile(request):
    """Redirect to user's own profile"""
    return redirect('user_profile', user_id=request.user.id)