from django.conf.urls import url, include
from . import views

app_name = 'music_app'

urlpatterns = [
    # /music
    url(r'^$', views.ViewIndex.as_view(), name="index"),
    
    # /music/album/id_number
     url(r'album/(?P<pk>[0-9]+)/$', views.DetailView.as_view() , name="detail"),
    
    # add new album from a form 
    # music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name="album-add"),
    
    # edit album
    url(r'(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name="album-update"),
    
     # delete album
     url(r'album/(?P<pk>\d+)/delete/$', views.AlbumDelete.as_view(), name="album-delete"),
    
    
    ]