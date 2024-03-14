from django.urls import path
from .import views

urlpatterns = [
    path('home2/',views.homePage2,name="homePage2"),
    path('registerImage/',views.registerImage,name="registerImage"),
    path('carImage/',views.carImage,name="carImage"),
]
