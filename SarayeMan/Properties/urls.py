from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)

urlpatterns = [
    path('', views.Home, name="Home"),
    path('property', views.Property_list,name="property"),
    path('property/<int:pk>', views.Property_detail, name="Property_detail"),
    path('CrudUser', views.CrudUser,name="CrudUser"),
    path('StateUser', views.StateUser, name="StateUser"),
    path('search', views.property_search, name="property_search"),
    path('about', views.AboutTemp, name="about"),
    path('NoneUsers', views.NoneUsers, name="NoneUsers"),
]

urlpatterns += router.urls