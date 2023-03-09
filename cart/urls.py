from django.urls import path
from .views import *


urlpatterns = [
    path('cart/', cart, name='cart'),
    # path('add_to_cart/', add_to_cart, name='cart')
]
