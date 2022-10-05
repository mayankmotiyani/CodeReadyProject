from django.db import models
from django.contrib.auth.models import User
from product.models import (
    Product
)

# Create your models here.

class Order(models.Model):
    # order_id = models.
    transaction_id = models.CharField(max_length=256)
    buyer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pass

