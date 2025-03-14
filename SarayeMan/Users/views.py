from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import LoginUser,RegisterUser,ForgetPassword
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from django.core.mail import send_mail
# Create your views here.
def UserView(request):
    forms=LoginUser()
    return render(request=request,template_name="login.html",context={"form":forms})

def register(request):
    forms=RegisterUser()
    return render(request=request,template_name="register.html",context={"form":forms})

def loginUserInWeb(request):
    if request.method == "POST":
        forms = LoginUser(request.POST)
        if forms.is_valid():
            username = forms.data["UserName"]
            password = forms.data["Password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request=request,template_name="login.html",context={"forms":forms, "success":"شما با موفقیت وارد شدین و الان می توانید به خرید هر یک از محصولات ما بپردازید و در صورت  لزوم پیام خود را برای ما ارسال کنید "} )
            else:
                return render(request=request,template_name="login.html",context={"forms":forms, "error":"نام کاربری یا رمز عبور اشتباه است "} )

    else:
        forms=LoginUser()
    return render(request=request,template_name="login.html",context={"form":forms})

def registerAction(request):
    if request.method=="POST":
        forms=RegisterUser(request.POST)
        if forms.is_valid():
            listourusers=User.objects.filter(email=forms.data["Email"]).all()
            if len(listourusers)>0:
                return render(request=request, template_name="register.html",context={"forms": forms, "error": "این کاربر وجود دارد"})
            else:
                user=User.objects.create_user(username=forms.data["UserName"],email=forms.data["Email"],password=forms.data["Password"])
                user.first_name=forms.data["Name"]
                user.last_name=forms.data["Family"]
                user.is_staff = False
                user.is_superuser = False
                user.save()
                customer_group,created = Group.objects.get_or_create(name="مشتریان")
                customer_group.user_set.add(user)
                return render(request=request,template_name="login.html",context={"forms":forms, "success":"شما با موفقیت ثبت نام شدین و پس از ورود می توانید به خرید هر یک از محصولات ما بپردازید و در صورت  لزوم پیام خود را برای ما ارسال کنید "} )
        else:
            return render(request=request, template_name="register.html",context={"forms": forms, "error":"هر یک از فیلد ها را به درستی وارد کنید"})


def CheckLogin(request):
    if request.user.is_authenticated:
        return HttpResponse("وارد شده است")
    else:
        return HttpResponse("وارد نشده است")

def LogOutUser(request):
    logout(request)
    return HttpResponseRedirect("/Users/")


def ForgetPasswords(request):
    if request.method == "POSst":
        form=ForgetPassword(request.POSt)
        if form.is_valid():
            username = form.cleaned_data.get("UserName")
            email = form.cleaned_data.get("Email")

            try:
                User.objects.get(username=username,email=email)

                send_mail(
                    'بازیابی رمز عور',
                'این ایمیل برای بازیابی رمز عبور شما ارسال شده است',
                'hamedkhodami977@gmail.com',
                [email],
                fail_silently=False)
                return render(request=request,template_name="password_rest_done.html",context={'email':email})
            except User.DoesNotExist:
                form.add_error(None,"کاربری با این مشخصات یافت نشد")
    else:
        form = ForgetPassword()
    return render(request=request,template_name="forget.html",context={'form':form})