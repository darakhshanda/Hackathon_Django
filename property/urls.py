from django.urls import path
from . import views

urlpatterns = [
    # ...other patterns...
    path('book/<int:property_id>/', views.book_property, name='book_property'),
]