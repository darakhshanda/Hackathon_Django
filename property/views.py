from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def property_list(request):
    # Logic to retrieve and display a list of properties
    if not request.user.is_staff:
        # Render a 403 Forbidden page for non-admin users
        return render(request, '403.html')
    else:
        return render(request, 'property_list.html')


@login_required()
def property_detail(request, pk):
    # Logic to retrieve and display details of a specific property
    if not request.user.is_staff:
        # Render a 403 Forbidden page for non-admin users
        return render(request, '403.html')
    else:
        return render(request, 'property_detail.html', {'pk': pk})


@login_required()
def property_create(request):
    # Logic to create a new property
    if not request.user.is_staff:
        # Render a 403 Forbidden page for non-admin users
        return render(request, '403.html')
    else:
        return render(request, 'property_form.html')
