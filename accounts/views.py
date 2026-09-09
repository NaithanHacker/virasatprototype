from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(email=email).exists():
            return render(request, 'accounts/register.html', {
                "error": "Email already exists"
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {
                "error": "Username already taken"
            })

        User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')

    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            user_obj = None

        user = None
        if user_obj is not None:
            user = authenticate(request, username=user_obj.username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            return render(request, "accounts/login.html", {
                "error": "Invalid email or password"
            })

    return render(request, "accounts/login.html")


def logout(request):
    auth_logout(request)
    return redirect("login")