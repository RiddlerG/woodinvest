from django.shortcuts import render, get_object_or_404
from django.views import View
from gallery.models import Album


class GalleryView(View):
    def get(self, request):
        gallery = Album.objects.filter(is_active=True)

        context = {
            'gallery': gallery,
        }

        return render(request, 'gallery/gallery.html', context)


class AlbumView(View):
    def get(self, request, album_slug):
        album = get_object_or_404(Album, slug=album_slug)
        
        context = {
            'album': album,
        }

        return render(request, 'gallery/album.html', context)
