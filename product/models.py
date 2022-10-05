from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

class ProductCategory(models.Model):
    category = models.CharField(max_length=256,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Product Category"

    def __str__(self):
        return "{}".format(self.category)


class ProductSubCategory(models.Model):
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=256,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Product Sub-Category"

    def __str__(self):
        return "{} : {}".format(self.category,self.subcategory)


class Product(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=256)
    product_description = models.TextField(blank=True,null=True)
    product_category = models.ForeignKey(ProductSubCategory,on_delete=models.CASCADE,blank=True,null=True)
    #missing fields : features,compatible_browser,themeforest_files,columns,tags
    product_price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    last_update = models.DateTimeField(auto_now=True,blank=True,null=True)
    published = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    is_high_resolution = models.BooleanField(_("isHighResolution"),default=False)
    is_documented = models.BooleanField(_("isDocumented"),default=False)
    is_responsive = models.BooleanField(_("isResponsive"),default=False)
    set_as_banner = models.BooleanField(_("setAsBanner"),default=False)
    set_as_top_category = models.BooleanField(_("setAsTopCategory"),default=False)
    

    class Meta:
        verbose_name_plural = "Product"

    # def get_absolute_url(self):
    #     return reverse('top-product', args=[str(self.id)])


    def __str__(self):
        return "{} : {}".format(self.product_name,self.owner.username.title())
