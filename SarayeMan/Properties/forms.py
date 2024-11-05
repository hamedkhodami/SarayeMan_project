from django import forms
from .models import PropertyModel
from django.core.validators import MinValueValidator
from captcha.fields import CaptchaField
class PropertyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        for item in PropertyForm.visible_fields(self):
            item.field.widget.attrs["class"] = "form-control"

    id = forms.CharField(widget=forms.HiddenInput, required=True, initial="0", label="")
    title=forms.CharField(required=True,min_length=5,max_length=200,label="عنوان")
    description=forms.CharField(required=True,widget=forms.Textarea,max_length=500,label="توضیحات")
    price=forms.DecimalField(required=True,max_digits=10,decimal_places=0,label="قیمت",validators=[MinValueValidator(0,message="لطفا عدد را به صورت منفی وارد نکنید")])
    address=forms.CharField(required=True,max_length=300,label="آدرس")
    area=forms.FloatField(required=True,label="مساحت",validators=[MinValueValidator(0,message="لطفا عدد را به صورت منفی وارد نکنید")])
    property_type=forms.ChoiceField(choices=PropertyModel.PROPERTY_TYPE_CHOICES,label="نوع آگهی")
    house_type=forms.ChoiceField(choices=PropertyModel.HOUSE_TYPE_CHOICES,label="نوع خانه")
    floor_number=forms.IntegerField(required=False,label="شماره طبقه",validators=[MinValueValidator(0,message="لطفا عدد را به صورت منفی وارد نکنید")])
    image=forms.ImageField(required=True,widget=forms.FileInput,help_text="",label="تصویر")
    garage=forms.IntegerField(required=True,label="تعداد گاراژ",validators=[MinValueValidator(0,message="لطفا عدد را به صورت منفی وارد نکنید")])
    bath=forms.IntegerField(required=True,label="تعداد سرویس بهداشتی",validators=[MinValueValidator(0,message="لطفا عدد را به صورت منفی وارد نکنید")])
    beds=forms.IntegerField(required=True,validators=[MinValueValidator(0,message="لطفا عدد را به صورت منفی وارد نکنید")],label="تعداد اتاق")
    amenities=forms.CharField(widget=forms.Textarea,required=True,label="امکانات دیگر")
    captcha = CaptchaField()



class PropertySearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PropertySearchForm, self).__init__(*args, **kwargs)
        for item in PropertySearchForm.visible_fields(self):
            item.field.widget.attrs["class"] = "form-control"

    title=forms.CharField(required=False,label="عنوان ملک",max_length=100)
    price_min=forms.DecimalField(required=False,label="حداقل قیمت",decimal_places=0,min_value=0)
    price_max=forms.DecimalField(required=False,label="حداکثر قیمت",decimal_places=0,min_value=0)
    area_min=forms.FloatField(required=False,label="حداقل مساحت",min_value=0)
    area_max=forms.FloatField(required=False,label="حداکثر مساحت",min_value=0)
    property_type=forms.ChoiceField(
        choices=[('','نوع ملک'),('for_sale','فروش'),('for_rent','اجاره'),('for_mortage','رهن')],
        required=False,label="نوع ملک"
    )