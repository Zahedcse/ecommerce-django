from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('single_page/<int:id>', single_product, name='single_product'),
    path('add_to_cart/<int:id>', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:id>', remove_from_cart, name='remove_from_cart'),
    path('decrease_quantity/<int:id>',
         decrease_quantity, name='decrease_quantity'),
    path('increase_quantity/<int:id>',
         increase_quantity, name='increase_quantity'),
    path('search/', search_results, name='search_results'),
]
