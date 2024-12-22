from django.urls import path
from . import views

urlpatterns = [
    path('slots/', views.view_slots, name='view_slots'),
    path('surf_sessions/book/<str:session_type>/', views.book_slot, name='book_slot'),
    path('my_bookings/', views.view_bookings, name='view_bookings'),

]