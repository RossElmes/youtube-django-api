from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'matchdetails',MatchdetailViewSet)
router.register(r'matchclips',MatchClipViewSet)
router.register(r'playlist',PlaylistViewSet)
router.register(r'playlistclips',PlaylistClipsViewSet)
router.register(r'codes',CodesViewSet)


urlpatterns = [
    path('',include(router.urls))
]