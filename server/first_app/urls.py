from django.urls import path
from rest_framework.routers import DefaultRouter
from first_app import views

default_router = DefaultRouter()
default_router.register('deep_tracks_viewset', views.DeepTracksViewSet)

urlpatterns = [
    path('helloworld', views.hello_world),
    path('hello', views.hello),
    path('album_view/', views.album_view),
    path('get_deep_albums/', views.get_deep_albums),
    path('track_view/', views.track_view),
    path('get_deep_tracks/', views.get_deep_tracks),
]

urlpatterns += default_router.urls
