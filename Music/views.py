from .models import Album, Song
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


def favourite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        render(request, "Music/details.html", {
            "album": album,
            "error_msg": "Sorry invalid input"
        })
    else:
        if not selected_song.is_favourite:
            selected_song.is_favourite = True
        else:
            selected_song.is_favourite = False
        selected_song.save()
    return render(request, "Music/detail.html", {"album": album})






















