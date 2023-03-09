from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse


from back.models import Banner, Product
from cart.models import Cart, CartItem

# Create your views here.


def home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    title = 'Home'
    full_name = request.user.get_full_name()
    all_products = Product.objects.all()
    banners = Banner.objects.all()
    return render(request, 'front/index.html', {'products': all_products, 'title': title, 'banners': banners, 'name': full_name})


def single_product(request, id):
    title = 'Details Page'
    product = Product.objects.filter(id=id).first()
    return render(request, 'front/single_details.html', {'title': title, 'product': product})


def add_to_cart(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart, product=product)

        if not item_created:
            cart_item.quantity += 1
            cart_item.save()
        cart.items.add(cart_item)

        return redirect(reverse('single_product', kwargs={'id': id}))
    else:
        return redirect(reverse('user_login'))


def remove_from_cart(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=id)
        cart = Cart.objects.get(user=request.user)
        cart_item = cart.items.filter(product=product).first()

        if cart_item is not None:
            cart_item.delete()
        cart.save()
        return redirect('cart')
    else:
        return redirect(reverse('user_login'))


def decrease_quantity(request, id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=id)
        cart = Cart.objects.get(user=request.user)
        cart_item = cart.items.filter(product=product).first()

        if cart_item is not None:
            cart_item.quantity -= 1
            if cart_item.quantity == 0:
                cart_item.delete()
            cart_item.save()
        cart.save()
        return redirect('cart')
    else:
        return redirect(reverse('user_login'))


def increase_quantity(request, id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=id)
        cart = Cart.objects.get(user=request.user)
        cart_item = cart.items.filter(product=product).first()

        if cart_item is not None:
            cart_item.quantity += 1
            cart_item.save()
        cart.save()
        return redirect('cart')
    else:
        return redirect(reverse('user_login'))
