import random
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import ChatModel,MessageModel
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from Properties.models import PropertyModel
# Create your views here.

@login_required(login_url="/NoneUsers")
def connect_to_random_consultant(request, property_id):
    if request.user.is_authenticated:

        property_instance = get_object_or_404(PropertyModel,id=property_id)
        consultants = User.objects.filter(groups__name="مشاوران")
        consultant = random.choice(consultants)

        chat, created = ChatModel.objects.get_or_create(property=property_instance,creator=request.user)
        if created:
            chat.participants.add(request.user,consultant)
        return redirect("chat_room",chat_id=chat.id)
    else:
        return redirect('/Users/')

@login_required(login_url="/NoneUsers")
def chat_room(request,chat_id):
    chat = get_object_or_404(ChatModel,id=chat_id,participants=request.user)
    if not chat.participants.filter(id=request.user.id).exists():
        raise PermissionDenied("شما اجازه دسترسی به این گفت و گو را ندارید")
    consultant= chat.participants.exclude(id=request.user.id).first()
    consultant_name = consultant.username if consultant else "مشاور ناشناس"
    property_title=chat.property.title
    previous_massages = MessageModel.objects.filter(chat=chat).order_by('sent_at')
    return render(request=request,template_name="room.html",context={'chat_id':chat.id,"consultant_name":consultant_name,"previous_massages":previous_massages,"property_title":property_title})

@login_required(login_url="/NoneUsers")
def RoomShow(request):
    listChat = ChatModel.objects.filter(participants=request.user)
    return render(request=request,template_name="chats.html",context={'listChat': listChat})
