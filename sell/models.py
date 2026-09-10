from django.db import models

# Create your models here.

class StoreArt(models.Model):
    name_of_art = models.CharField(max_length=150, null=True)
    name_of_artist = models.CharField(max_length=150, null=True)
    price_of_art = models.IntegerField()
    desc_of_art = models.TextField()
    image_of_art = models.ImageField()

    def __str__(self):
            return self.name_of_art