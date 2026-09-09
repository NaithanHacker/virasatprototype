from django.shortcuts import render

# Create your views here.

def info_view(request):
    return render(request, 'info.html')