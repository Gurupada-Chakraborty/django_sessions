from .models import Album, Song
from django.views import generic
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from .form import UserForm

class IndexView(generic.ListView):
    template_name = 'Music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'Music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    #fields = ['artist', 'album_name', 'genre', 'album_logo']
    fields = '__all__'

class AlbumUpdate(UpdateView):
    model = Album
    fields = '__all__'
    #success_url = reverse_lazy("Music:index")

class AlbumDelete(DeleteView):
    model = Album
    fields = '__all__'
    success_url = reverse_lazy("Music:index")

class AlbumEditView(generic.ListView):
    template_name = 'Music/edit-album.html'

    def get_queryset(self):
        return Album.objects.all()

class SongCreate(CreateView):
    model = Song
    fields = '__all__'


def favourite_album(request, album_id):
    all_albums = Album.objects.all()
    try:
        album = Album.objects.get(pk=request.POST['album_id'])
    except (KeyError, Album.DoesNotExist):
        return render(request, 'Music/index.html', {KeyError: 'invalid', 'all_albums': all_albums })
    else:
        context = {'album': album, 'all_albums': all_albums}
        if not album.is_favourite:
            album.is_favourite = True
        else:
            album.is_favourite = False
        album.save()

        return render(request, 'Music/index.html', context)


class SongDelete(DeleteView):
    model = Song
    fields = '__all__'
    success_url = reverse_lazy('Music:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'Music/registration.html'

    #gets the registration form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    #processes the registration form details to the database
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #authenticate the user and login
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.user.username
                    return redirect('Music:index')

        else:
            return render(request, self.template_name, {'form': form})






















