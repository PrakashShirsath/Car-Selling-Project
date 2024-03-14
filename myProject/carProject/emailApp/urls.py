from django.urls import path
from . import views
urlpatterns = [
    path('',views.emailPage,name = 'emailPage'),
    path('save/',views.sendEmail,name = 'sendEmail'),
]
