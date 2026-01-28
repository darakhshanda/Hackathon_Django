from django.urls import path
from . import views
urlpatterns = [
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/', views.my_profile, name='my_profile'), 
    path('profile/delete/', views.delete_profile, name='delete_profile'),
    path('profiles/', views.user_profiles_list,
         name='user_profiles_list'),  # List all profiles Admin view
]
