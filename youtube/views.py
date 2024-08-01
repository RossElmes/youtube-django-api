from rest_framework import viewsets
from .models import *
from .serializers import *
from .filters import MatchClipFilter,PlaylistClipFilter
from django_filters import rest_framework as filters

# Create your views here.

class MatchdetailViewSet(viewsets.ModelViewSet):
    queryset = MatchDetail.objects.all()
    serializer_class = MatchDetailSerializer

class MatchClipViewSet(viewsets.ModelViewSet):
    queryset = MatchClip.objects.all()
    serializer_class = MatchClipSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MatchClipFilter

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class PlaylistClipsViewSet(viewsets.ModelViewSet):
    queryset = PlaylistClips.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PlaylistClipFilter

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PlaylistClipCreateSerializer
        return PlaylistClipsSerializer


class CodesViewSet(viewsets.ModelViewSet):
    queryset = Codes.objects.all()
    serializer_class = CodesSerializer