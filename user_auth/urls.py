from django.urls import path
from .views import *

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('registration/', user_signup, name='user_signup'),
    path('user_logout/', user_logout, name='user_logout'),
]
