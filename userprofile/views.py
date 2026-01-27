from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileSetupForm

# Create your views here.
# Profile Setup


def index(request):
    return render(request, 'index.html')


@login_required()
def profile_setup(request):
    if request.method == 'POST':
        form = ProfileSetupForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('index', user_id=request.user.id)
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
            return redirect('index', user_id=request.user.id)
    else:
        form = ProfileSetupForm(instance=request.user.userprofile)
    return render(request, 'userprofile/profile_edit.html', {'form': form})


@login_required()
def user_profile(request, user_id):
    from django.contrib.auth.models import User
    user = User.objects.get(id=user_id)
    is_admin = request.user.is_staff or request.user.is_superuser
    return render(request, 'userprofile.html', {
        'profile_user': user,
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
