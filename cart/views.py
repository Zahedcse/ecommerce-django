from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Cart, Product

# Create your views here.


def cart(request):
    if request.user.is_authenticated:
        title = 'Cart | Details'
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=request.user)
        items = cart.items.all()
        user = request.user
        total = cart.total_price()
        return render(request, 'cart/cart.html', {'title': title, 'items': items, 'user': user, 'total': total})
    else:
        return redirect(reverse('user_login'))
