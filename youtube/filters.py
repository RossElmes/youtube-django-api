import django_filters
from .models import MatchClip

class MatchClipFilter(django_filters.FilterSet):
    match = django_filters.CharFilter(field_name="match", lookup_expr='exact')

    class Meta:
        model = MatchClip
        fields = ['match']