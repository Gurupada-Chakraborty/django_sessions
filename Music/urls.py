from django.urls import re_path
from . import views

app_name = "Music"


urlpatterns = [
    #/music/
    re_path(r'^$', views.IndexView.as_view(), name='index'),

    #/music/732
    re_path(r'^album/details/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),

    re_path(r'^album/add/$', views.AlbumCreate.as_view(), name='add-album'),

    re_path(r'^album/edit/$', views.AlbumEditView.as_view(), name='edit-album'),

    re_path(r'^album/edit/update/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='update-album'),

    re_path(r'^album/delete/(?P<pk>[0-9]+)/$', views.AlbumDelete.as_view(), name='delete-album'),

    re_path(r'^album/song/add/(?P<pk>[0-9]+)/$', views.SongCreate.as_view(), name='add-song'),

    re_path(r'^album/fav/(?P<album_id>[0-9]+)/$', views.favourite_album, name='fav-album'),

    re_path(r'^album/song/delete/(?P<pk>[0-9]+)/$', views.SongDelete.as_view(), name='del-song'),

    re_path(r'^register/$', views.UserFormView.as_view(), name='register-user'),

    ]


