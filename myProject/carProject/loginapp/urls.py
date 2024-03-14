from django.urls import path
from . import views

urlpatterns = [
	path('',views.homePage,name="homePage"),
	path('signup/',views.signUpPage,name="signUpPage"),
	path('login/',views.loginPage,name="loginPage"),
]
