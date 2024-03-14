from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import User


def homePage(request):
    return render(request, "loginapp/signup.html")


def signUpPage(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1 != pass2:
            return HttpResponse("Your Password and Confirm Password do not match")
        else:
            my_user = User.objects.create(username=uname, email=email, password=pass1)
            my_user.save()
            return redirect("loginPage")
    return render(request, "loginapp/signup.html")


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    login(request, user)
                    return redirect('homePage')
                else:
                    return HttpResponse("Username or Password is incorrect", status=401)
            except User.DoesNotExist:
                return HttpResponse("Username or Password is incorrect", status=401)
        else:
            return HttpResponse("Please provide both username and password", status=400)

    return render(request, "loginapp/login.html")