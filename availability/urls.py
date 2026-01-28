from django.urls import path
from . import views
urlpatterns = [
    path('', views.availability_list, name='availability_list'),
    path('<int:pk>/', views.availability_detail,
         name='availability_detail'),
    path('create/', views.availability_weekly,
         name='availability_create'),
]
