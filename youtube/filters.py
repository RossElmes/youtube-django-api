import django_filters
from .models import MatchClip, PlaylistClips

class MatchClipFilter(django_filters.FilterSet):
    match = django_filters.CharFilter(field_name="match", lookup_expr='exact')

    class Meta:
        model = MatchClip
        fields = ['match']

class PlaylistClipFilter(django_filters.FilterSet):
    playlist = django_filters.CharFilter(field_name="playlist", lookup_expr='exact')

    class Meta:
        model = PlaylistClips
        fields = ['playlist']