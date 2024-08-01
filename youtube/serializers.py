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
    clip = MatchClipSerializer(read_only=True)       # Nested detailed representation
    playlist = PlaylistSerializer(read_only=True)  # Nested detailed representation

    class Meta:
        model = PlaylistClips
        fields = ['id', 'video_id', 'clip', 'playlist']

class PlaylistClipCreateSerializer(serializers.ModelSerializer):
    clip = serializers.PrimaryKeyRelatedField(queryset=MatchClip.objects.all())
    playlist = serializers.PrimaryKeyRelatedField(queryset=Playlist.objects.all())

    class Meta:
        model = PlaylistClips
        fields = ['video_id', 'clip', 'playlist']

class CodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codes
        fields = '__all__'