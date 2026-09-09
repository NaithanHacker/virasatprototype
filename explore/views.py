from django.shortcuts import render, redirect
from explore.models import Art
from accounts.models import User

def art_add(request):
    if request.method == "POST":
        name_artist = request.POST['name_artist']
        name_art = request.POST['name_art']
        description_art = request.POST['desc_art']
        image_art = request.FILES['image_art']   

        Art.objects.create(
            name_artist=name_artist,
            name_art=name_art,
            description_art=description_art,
            image_art=image_art
        )
        return redirect('explore')
    return render(request, 'artadd.html')


def explore(request):
    arts = Art.objects.all()
    return render(request, 'explore.html', {'arts': arts})