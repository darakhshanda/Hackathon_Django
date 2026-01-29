from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.property_list, name='property_list'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    # New URL pattern for creating a property Admin job
    path('property/create/', views.property_create, name='property_create'),
]
