from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    title = 'User Login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'auth/login.html', {'error': 'User not found'})
        if user is not None:
            login(request, user)
            return redirect('home')
    else:
        return render(request, 'auth/login.html', {'title': title})


def user_signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    title = 'User Sign Up'
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            return render(request, 'auth/login.html', {'error': 'Password Not Matched'})
        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                        username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user_login')
    else:
        return render(request, 'auth/registration.html', {'title': title})


def user_logout(request):
    logout(request)
    return redirect('user_login')
