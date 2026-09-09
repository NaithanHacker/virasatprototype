from django.db import models

# Create your models here.

class Art(models.Model):
    name_artist = models.CharField(max_length=100, null=True)
    name_art = models.CharField(max_length=200)
    description_art = models.TextField()
    image_art = models.ImageField()
    

    def __str__(self):
        return self.name_art