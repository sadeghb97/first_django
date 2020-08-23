from rest_framework import serializers
from django.db import models
from first_app import models as first_app_models


class AlbumRelatedSerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = first_app_models.Album
        fields = ('album_name', 'artist', 'tracks')


class AlbumSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = first_app_models.Album
        fields = "__all__"


class TrackSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = first_app_models.Track
        fields = "__all__"


class TrackDeepSerializer(serializers.ModelSerializer):
    #khate code bad va meghdar dehie depth ba yek, yek kar ra anjam midahand
    album = AlbumSimpleSerializer()

    class Meta:
        model = first_app_models.Track
        fields = "__all__"
        # depth = 1
