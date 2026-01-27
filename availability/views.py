from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def availability_list(request):
    return render(request, 'availability/availability_list.html')

@login_required()
def availability_detail(request, pk):
    return render(request, 'availability/availability_detail.html', {'pk': pk})
@login_required()
def availability_weekly(request):
    return render(request, 'availability/availability_form.html')

