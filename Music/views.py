from django.http import HttpResponse


def index(request):
    html = "<h1> this is Music home."
    return HttpResponse(html)





















