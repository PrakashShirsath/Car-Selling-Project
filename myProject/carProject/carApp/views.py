from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import userProduct

# Create your views here.
def homePage2(request):
	return render(request,"carApp/index.html");

def registerImage(request):
	if request.method == 'POST':
		imgName = request.POST ['imgname']
		imgMode = request.POST ['imgmode']
		imgModel = request.POST ['imgmodel']
		imgVariant = request.POST ['imgvariant']
		imgPrice = request.POST ['imgprice']
		imgPick = request.POST ['imgpick']
		
		user = userProduct.objects.create(imgName = imgName,imgMode = imgMode, imgModel = imgModel, imgVariant = imgVariant, imgPrice = imgPrice,imgPick = imgPick)
	return render(request,'carApp/regisImg.html');		

def carImage(request):
	carCollection = userProduct.objects.all();
	return render(request,'carApp/carImg.html',{'carCollection':carCollection});	

 