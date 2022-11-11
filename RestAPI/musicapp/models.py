from django.db import models

# Create your models here.
class artiste(models.Model):
    artist = models.CharField(max_length=10)
    song  = models.CharField(max_length=10)
    artiste_id = models.IntegerField()

    def __str__(self):
        return self.artist +' '+ self.song

