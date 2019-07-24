from .models import Album
from django.shortcuts import render, get_object_or_404
from django.http import Http404


def index(request):
    all_albums = Album.objects.all()
    context = {"all_albums": all_albums}
    return render(request, 'Music/index.html', context)


def details(request, album_id):
    #try:
    #album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    #except:
    #raise Http404("Album does not exist!")
    album = get_object_or_404(Album, pk=album.id)
    return render(request, "Music/detail.html", {"album": album})





















