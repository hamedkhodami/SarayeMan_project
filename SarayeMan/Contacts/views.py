from django.shortcuts import render
from .models import ContactUS
from .forms import ContactUsFrom
from django.http import HttpResponse
# Create your views here.



def SaveAsk(request):
    print(request.method)
    if request.method=="POST":
        forms=ContactUsFrom(request.POST)
        if forms.is_valid():
            NewCommnet = ContactUS(Fullname=forms.cleaned_data["Fullname"], Phone=forms.cleaned_data["Phone"]
                                    , Email=forms.cleaned_data["Email"], Message=forms.cleaned_data["Message"])
            NewCommnet.save()
            forms = ContactUsFrom()
            return render(request=request,template_name="contact.html",context={"forms":forms, "success":" نظر شما با موفقیت ارسال شد و از طریق ایمیل و پیامک به شما در اسرع وقت پاسخ داده خواهد شد"} )
        else:
            return render(request=request,template_name="contact.html",context={"forms":forms, "error":"خطا در اعتبار سنجی فرم "} )

    else:
        forms = ContactUsFrom()
    return render(request=request,template_name="contact.html",context={"forms":forms})