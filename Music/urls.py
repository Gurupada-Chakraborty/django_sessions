from django.urls import re_path
from . import views

urlpatterns = [
    #/music/
    re_path(r'^$', views.index, name='index'),

    #/music/732
    re_path(r'^(?P<album_id>[0-9]+)/$', views.details, name="details")
]