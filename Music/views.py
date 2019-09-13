from .models import Album, Song
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'Music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'Music/detail.html'
























