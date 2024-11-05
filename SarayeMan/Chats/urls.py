from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomShow,name="RoomShow"),
    path('connect/<int:property_id>/',views.connect_to_random_consultant,name='connect_to_random_consultant'),
    path('chat/<int:chat_id>/',views.chat_room,name='chat_room')

]