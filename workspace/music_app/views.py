from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404 , redirect
from django.http import HttpResponse
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . models import Album, Song
from .forms import UserForm


# Generic views
class ViewIndex(generic.ListView):
    
    template_name = "music_app/index.html"
    context_object_name = 'all_album'
    
    def get_queryset(self):
        
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music_app/details.html'

# view album page
class AlbumCreate(CreateView):
    model = Album
    fields = ['album_title', 'artist', 'genre', 'album_logo']
    

# for editing the page
class AlbumUpdate (generic.UpdateView):
    model = Album
    fields = ['album_title', 'artist', 'genre', 'album_logo']
    success_url  = reverse_lazy('music_app:index')
    
# delete page
class AlbumDelete(DeleteView):
    model= Album
    success_url  =  reverse_lazy('music_app:index')

    
    