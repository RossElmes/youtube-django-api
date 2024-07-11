from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(MatchDetail)
admin.site.register(MatchClip)
admin.site.register(Playlist)
admin.site.register(PlaylistClips)
admin.site.register(Codes)