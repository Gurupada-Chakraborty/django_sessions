from django.urls import re_path
from . import views

app_name = "Music"


urlpatterns = [
    #/music/
    re_path(r'^$', views.IndexView.as_view(), name='index'),

    #/music/732
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),

    re_path(r'^album/add/$', views.AlbumCreate.as_view(), name='add-album'),

    re_path(r'^album/edit/$', views.AlbumEditView.as_view(), name='edit-album'),

    re_path(r'^album/edit/update/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='update-album'),

    re_path(r'^album/delete/(?P<pk>[0-9]+)/$', views.AlbumDelete.as_view(), name='delete-album'),

    re_path(r'^song/add/(?P<pk>[0-9]+)/$', views.SongCreate.as_view(), name='add-song'),

    ]


