from django.db import models
from django.contrib.auth.models import User
from django_jalali.db.models import jDateTimeField
from PIL import Image
# Create your models here.

class PropertyModel(models.Model):
    PROPERTY_TYPE_CHOICES=[
        ('for_rent','اجاره'),
        ('for_sale','فروش'),
        ('for_mortage','رهن'),
    ]
    HOUSE_TYPE_CHOICES=[
        ('آپارتمانی','آپارتمانی'),
        ('ویلایی','ویلایی')
    ]

    title= models.CharField(max_length=200,verbose_name="عنوان")
    description= models.TextField(max_length=500,verbose_name="توضیحات")
    price= models.DecimalField(max_digits=10,decimal_places=0,verbose_name="قیمت")
    address=models.CharField(max_length=300,verbose_name="آدرس")
    area=models.FloatField(verbose_name="مساحت")
    property_type=models.CharField(max_length=20,choices=PROPERTY_TYPE_CHOICES,verbose_name="نوع آگهی")
    house_type=models.CharField(max_length=20,choices=HOUSE_TYPE_CHOICES,verbose_name="نوع خانه")
    floor_number=models.IntegerField(null=True,blank=True,verbose_name="شماره طبقه")
    date_posted=jDateTimeField(auto_now_add=True,verbose_name="اضافه شده در تاریخ")
    image=models.ImageField(upload_to="files/images",verbose_name="تصویر")
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر")
    garage=models.IntegerField(default=0,verbose_name="تعداد گاراژ")
    bath=models.IntegerField(default=0,verbose_name="تعداد حمام")
    beds=models.IntegerField(default=0,verbose_name="تعداد اتاق خواب")
    amenities=models.TextField(blank=True,verbose_name="امکانات")

    class Meta:
        verbose_name = "ملک"
        verbose_name_plural = "املاک"

    def save(self,*args,**kwargs):
        if self.house_type ==  'ویلایی' :
            self.floor_number = None
        super(PropertyModel,self).save(*args,**kwargs)
        img = Image.open(self.image.path)
        img = img.resize((600,800), Image.LANCZOS)
        img.save(self.image.path)


