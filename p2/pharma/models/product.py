from django.db import models
from .catagory import Catagory


class Product(models.Model):

    pname = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()


