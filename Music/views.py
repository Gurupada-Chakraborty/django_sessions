from django.http import HttpResponse
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    html = '<html><h2>List : </h2><br>'
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<html><a href="' + url + '">' + str(album.album_name) + '</a><br><html>'
    return HttpResponse(html)


def details(request, album_id):
    html = "<html><h1> This album has id : " + str(album_id) + "</h1></html>"
    return HttpResponse(html)




















