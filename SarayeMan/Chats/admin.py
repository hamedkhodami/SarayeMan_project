from django.contrib import admin
from .models import MessageModel,ChatModel
# Register your models here.

@admin.register(ChatModel)
class ChatModelAdmin(admin.ModelAdmin):
    list_display = ('id','created_at')


@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ('chat','sender','message','sent_at')
    list_filter =  ('chat','sender')
    search_fields = ('sender__username','message')

    def save_model(self, request, obj, form, change):
        if not obj.sender:
            obj.sender = request.user
        super().save_model(request,obj,form,change)

