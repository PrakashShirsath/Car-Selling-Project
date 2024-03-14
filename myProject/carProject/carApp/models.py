from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userProduct(models.Model):
	imgName = models.CharField(max_length=30)
	imgMode = models.CharField(max_length=30)
	imgModel = models.IntegerField()
	imgVariant = models.CharField(max_length=30)
	imgPrice = models.DecimalField(max_digits=10, decimal_places=2)
	imgPick = models.ImageField(upload_to = 'images/')

	def __str__(self):
		return self.imgName

