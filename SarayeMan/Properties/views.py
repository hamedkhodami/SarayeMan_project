from django.core.paginator import Paginator
from django.shortcuts import render,redirect,get_object_or_404
from .forms import PropertyForm,PropertySearchForm
from .models import PropertyModel
from django.contrib.auth.decorators import login_required
from .UserAuth import UserAuth
from rest_framework import viewsets
from .serializers import PropertySerializer
from django.db.models import Q,Value
from django.db.models.functions import Replace
from decimal import Decimal
# Create your views here.


def Home(request):
    properties=PropertyModel.objects.order_by('-date_posted')[:6]
    return render(request=request,template_name="index.html",context={"properties":properties})

def Property_list(request):
    property_type=request.GET.get('category')
    if property_type:
        properties=PropertyModel.objects.filter(property_type=property_type,).order_by('-date_posted')
    else:
        properties=PropertyModel.objects.all().order_by('-date_posted')

    pagingtor=Paginator(properties,6)
    page_number = request.GET.get('page',1)
    page_obj=pagingtor.get_page(page_number)

    return render(request=request,template_name="property-grid.html",context={'page_obj':page_obj})

@login_required(login_url="/NoneUsers")
def CrudUser(request):
    properties=PropertyModel.objects.filter(user=request.user).order_by('-date_posted')
    if request.method == "POST":
            form = PropertyForm(request.POST,request.FILES)
            if form.is_valid():
                property_instance= PropertyModel(
                    title=form.cleaned_data['title'],
                    description=form.cleaned_data['description'],
                    price=form.cleaned_data['price'],
                    address=form.cleaned_data['address'],
                    area=form.cleaned_data['area'],
                    property_type=form.cleaned_data['property_type'],
                    house_type=form.cleaned_data['house_type'],
                    floor_number=form.cleaned_data['floor_number'],
                    image=form.cleaned_data['image'],
                    garage=form.cleaned_data['garage'],
                    bath=form.cleaned_data['bath'],
                    beds=form.cleaned_data['beds'],
                    amenities=form.cleaned_data['amenities'],
                    user=request.user
                )
                property_instance.save()
                return redirect('CrudUser')
    else:
        form = PropertyForm()

    return render(request=request,template_name="functionUser.html",context={'form':form,'properties':properties})

def StateUser(request):
    user_st=UserAuth().StateLogin(request)
    if user_st["State"]:
        return render(request=request,template_name="AuthUser.html",context={"user_st":user_st})
    else:
        return render(request=request,template_name="noneUser.html")

def NoneUsers(request):
    return render(request=request,template_name="noneUser.html")

def AboutTemp(request):
    return render(request=request,template_name="about.html")

def Property_detail(request,pk):
    property = get_object_or_404(PropertyModel,pk=pk)
    min_price=property.price * Decimal(0)
    max_price=property.price * Decimal(1)
    similar_properties = PropertyModel.objects.filter(
        Q(house_type__iexact=property.house_type) &
        Q(property_type__iexact=property.property_type) &
        Q(price__gte=min_price, price__lte=max_price)
    ).exclude(pk=pk)[:3]
    return render(request=request,template_name="property-single.html",context={'property':property,'similar_properties':similar_properties})

def property_search(request):
    form = PropertySearchForm(request.GET)
    properties=PropertyModel.objects.all()
    if form.is_valid():
        title = form.cleaned_data.get('title')
        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')
        area_min = form.cleaned_data.get('area_min')
        area_max = form.cleaned_data.get('area_max')
        property_type = form.cleaned_data.get('property_type')

        if title:
            title_without_space = title.replace(" ", "")
            properties = properties.annotate(
                title_no_spaces = Replace('title' ,Value(' '),Value(''))
            ).filter(Q(title__icontains=title_without_space))
        if price_min:
            properties =  properties.filter(price__gte=price_min)
        if price_max:
            properties = properties.filter(price__lte=price_max)
        if area_min:
            properties = properties.filter(area__gte=area_min)
        if area_max:
            properties = properties.filter(area__lte=area_max)
        if property_type:
            properties = properties.filter(property_type=property_type)

    return render(request=request,template_name="search_results.html",context={"form":form,"properties":properties})


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = PropertyModel.objects.all()
    serializer_class = PropertySerializer


