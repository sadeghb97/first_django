from rest_framework import serializers
from server.first_app import models

class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True, on_delete=models.CASCADE)

    class Meta:
        model = models.Album
        fields = ('album_name', 'artist', 'tracks')