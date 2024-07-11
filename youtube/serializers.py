from rest_framework import serializers
from .models import *


class MatchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchDetail
        fields = '__all__'

class MatchClipSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchClip
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class PlaylistClipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistClips
        fields = '__all__'

class CodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codes
        fields = '__all__'