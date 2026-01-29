from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from property.models import Property

# Create your views here.


def property_list(request):

    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})


def property_detail(request, pk):
    # Logic to retrieve and display details of a specific property

    property = Property.objects.get(pk=pk)
    return render(request, 'property_detail.html', {'property': property})


@login_required()
def property_create(request):
    # Logic to create a new property
    if not request.user.is_staff:
        # Render a 403 Forbidden page for non-admin users
        return render(request, )
    else:
        return render(request, 'property_form.html')
