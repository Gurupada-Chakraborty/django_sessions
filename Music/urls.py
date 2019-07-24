from django.urls import re_path
from . import views

app_name = "Music"


urlpatterns = [
    #/music/
    re_path(r'^$', views.index, name='index'),

    #/music/732
    re_path(r'^(?P<album_id>[0-9]+)/$', views.details, name="details"),

    #/music/<album_id>/favourite
    re_path(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name="favourite")

    ]


