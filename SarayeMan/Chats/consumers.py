from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import ChatModel,MessageModel
from django.contrib.auth.models import User
import json


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id=self.scope['url_route']['kwargs']['chat_id']
        self.room_group_name = f'chat_{self.chat_id}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json=json.loads(text_data)
        message=text_data_json['message']
        sender_username= text_data_json['sender']
        chat= await sync_to_async(ChatModel.objects.get, thread_sensitive=True)(id=self.chat_id)
        sender= await sync_to_async(User.objects.get,thread_sensitive=True)(username=sender_username)
        await sync_to_async(MessageModel.objects.create,thread_sensitive=True)(
            chat=chat,
            sender=sender,
            message=message
        )
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": 'chat_message',
                "message": f"{sender.username}: {message}"
            }
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))