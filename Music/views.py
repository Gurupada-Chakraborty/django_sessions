from django.http import HttpResponse


def index(request):
    html = "<html><h1> This displays list of albums"
    return HttpResponse(html)


def details(request, album_id):
    html = "<html><h1> This album has id : " + str(album_id)
    return HttpResponse(html)




















