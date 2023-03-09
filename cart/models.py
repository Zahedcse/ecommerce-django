from django.db import models
from back.models import *
from django.contrib.auth.models import User


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name + "-" + str(self.quantity)

    def total_price(self):
        return self.product.price * self.quantity


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)

    def __str__(self):
        return self.user.username

    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.total_price()
        return total
