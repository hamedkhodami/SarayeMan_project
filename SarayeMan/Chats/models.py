from django.db import models
from django.contrib.auth.models import User
from django_jalali.db.models import jDateTimeField
from Properties.models import PropertyModel
# Create your models here.

class ChatModel(models.Model):
    participants=models.ManyToManyField(User,verbose_name="شرکت کنندگان")
    created_at=jDateTimeField(auto_now_add=True,verbose_name="زمان ایجاد")
    property = models.ForeignKey(PropertyModel,on_delete=models.CASCADE,verbose_name="ملک مرتبط", null=True)
    creator = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="ایجاد کننده",related_name="created_chats")

    class Meta:
        verbose_name="گفتگو"
        verbose_name_plural="گفتوگوها"

class MessageModel(models.Model):
    chat=models.ForeignKey(ChatModel,on_delete=models.CASCADE,related_name="messages",verbose_name="گفتگو")
    sender=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="فرستنده")
    message=models.TextField(verbose_name="پیام")
    sent_at=jDateTimeField(auto_now_add=True,verbose_name="زمان ارسال")

    class Meta:
        verbose_name="پیام"
        verbose_name_plural="پیام ها"
