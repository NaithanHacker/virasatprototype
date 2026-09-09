from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html', {
        "user": request.user
        })