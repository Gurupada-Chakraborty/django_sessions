from .models import Album
from django.shortcuts import render
from django.http import Http404


def index(request):
    all_albums = Album.objects.all()
    context = {"all_albums": all_albums}
    return render(request, 'Music/index.html', context)


def details(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, "Music/detail.html", {"album": album})





















