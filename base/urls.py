from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('room-form/', views.roomForm, name='room-form'),
    path('update-room/<int:pk>', views.updateRoom, name='update-room'),
    path('delete-room/<int:pk>', views.deleteRoom, name='delete-room'),
]
