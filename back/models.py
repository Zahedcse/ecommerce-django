from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/product')

    def __str__(self):
        return self.name


class Banner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/banners')

    def __str__(self):
        return self.name
