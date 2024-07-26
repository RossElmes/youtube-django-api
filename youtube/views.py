from rest_framework import viewsets
from .models import *
from .serializers import *
from .filters import MatchClipFilter
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
    serializer_class = PlaylistClipsSerializer


class CodesViewSet(viewsets.ModelViewSet):
    queryset = Codes.objects.all()
    serializer_class = CodesSerializer