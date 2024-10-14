from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.registerpage, name='register'),
    path('room/<str:pk>/', views.room, name='room'),
    path('createroom/', views.createroom, name='createroom'),
    path('updateroom/<str:pk>/', views.updateroom, name='updateroom'),
    path('deleteroom/<str:pk>/', views.deleteroom, name='deleteroom'),
    path('deleteMessage/<str:pk>/', views.deleteMessage, name='deleteMessage'),
    path('profile/<str:pk>/', views.userprofile, name='profile'),
     path('update-user/', views.updateUser, name="update-user"),
    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
    path('videocall/', views.videocall, name="videocall"),
]
