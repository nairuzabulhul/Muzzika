from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse 

# Create your models here..

# Albums
class Album(models.Model):
    
    album_title =  models.CharField(max_length=500)
    artist = models.CharField(max_length=500)
    genre  = models.CharField(max_length=1000)
    album_logo= models.FileField() # upload a file
    
    
    def get_absolute_url(self):
        return reverse('music_app:detail', kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.album_title + "-" + self.artist


# # Songs
class Song(models.Model):
    album= models.ForeignKey(Album, on_delete= models.CASCADE)
    song_title= models.CharField(max_length=500)
    file_type=models.CharField(max_length=100)
    is_favorite= models.BooleanField(default=False)
    
    def __str__(self):
        
        return self.song_title 
 