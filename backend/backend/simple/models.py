from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=30, null=True, blank=False)
    brand = models.CharField(max_length=30, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=30, null=True, blank=True)
    price = models.DecimalField(max_digits = 10, decimal_places=2,default=0)
    sku = models.CharField(max_length=30, null=True, blank=False)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.name

class Copies(models.Model):
    _id = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    sizeCp = models.DecimalField(max_digits = 5, decimal_places=1, blank=False)
    stockCp = models.IntegerField(null=True, blank=False,default=0)
    def __str__(self):
        return str(self._id)




#user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)