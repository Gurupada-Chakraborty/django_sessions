from django.http import HttpResponse
from .models import Album
from django.template import loader


def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template("Music/index.html")
    context = {
        "all_albums": all_albums
    }
    return HttpResponse(template.render(context, request))


def details(request, album_id):
    html = "<html><h1> This album has id : " + str(album_id) + "</h1></html>"
    return HttpResponse(html)




















