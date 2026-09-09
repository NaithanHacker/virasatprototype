from django.shortcuts import render, redirect
from sell.models import StoreArt
# Create your views here.

def art_add(request):
    if request.method == "POST":
        name_of_art = request.POST['name_of_art']
        name_of_artist = request.POST['name_of_artist']
        price_of_art = request.POST['price_of_art']
        desc_of_art = request.POST['desc_of_art']
        image_of_art = request.FILES['image_of_art']   

        StoreArt.objects.create(
            name_of_art=name_of_art,
            name_of_artist=name_of_artist,
            price_of_art=price_of_art,
            desc_of_art=desc_of_art,
            image_of_art=image_of_art
        )
        return redirect('sell')
    return render(request, 'artsell.html')


def sell(request):
    items = StoreArt.objects.all()
    return render(request, 'sell.html', context={"items":items})