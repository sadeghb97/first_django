from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework import viewsets

from .models import Album, Track
from .serializers import *


@api_view(['POST', 'GET'])
def album_view(request):
    if request.method == "GET":
        albums = Album.objects.all()
        ser = AlbumSimpleSerializer(albums, many=True)
        return Response(ser.data, status.HTTP_200_OK)

    elif request.method == "POST":
        ser = AlbumSimpleSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_deep_albums(request):
    albums = Album.objects.all()
    ser = AlbumRelatedSerializer(albums, many=True)
    return Response(ser.data, status.HTTP_200_OK)


@api_view(['POST', 'GET'])
def track_view(request):
    if request.method == "GET":
        albums = Track.objects.all()
        ser = TrackSimpleSerializer(albums, many=True)
        return Response(ser.data, status.HTTP_200_OK)

    elif request.method == "POST":
        ser = TrackSimpleSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_deep_tracks(request):
    albums = Track.objects.all()
    ser = TrackDeepSerializer(albums, many=True)
    return Response(ser.data, status.HTTP_200_OK)


@api_view()
def hello_world(request):
    return Response({'message': "Hello RestDjango!!!"})


@api_view(['GET', 'POST'])
def hello(request):
    if "name" in request.data:
        return Response({'message': "Hello dear {}".format(request.data['name'])}, status=status.HTTP_200_OK)
    elif "name" in request.GET:
        return Response({'message': "Hi dear {}".format(request.GET['name'])}, status=status.HTTP_200_OK)
    else:
        return Response({'message': "Hello friend"}, status=status.HTTP_200_OK)


#ba hamin chand khat code mitavan tracke jadid ezafe kard
#tracki ra hazf kard ya update kard ya hazf kard
#agar mikhahid karkard haye pishfarz taghir konad bayad method haye an ra override konid
#tamame method haye piade shode az in dast hastand va vojudeshan zaruri nist
class DeepTracksViewSet (viewsets.ModelViewSet):
    queryset = Track.objects.all()
    http_method_names = ['post', 'put', 'get', 'delete']
    # serializer_class = TrackDeepSerializer --> yek method baraye an override mikonim

    def get_serializer_class(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return TrackSimpleSerializer
        else:
            return TrackDeepSerializer

    def list(self, request, *args, **kwargs):
        objs = super().list(request, *args, **kwargs)
        print("---- List ----")
        return objs

    def create(self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        print("---- Create ----")
        return obj

    def update(self, request, *args, **kwargs):
        obj = super().update(request, *args, **kwargs)
        instance = self.get_object()
        print("---- Update : {}".format(instance.title))
        return obj

    def retrieve(self, request, *args, **kwargs):
        obj = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        print("---- Retrieve : {}".format(instance.title))
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print("---- Destroy : {}".format(instance.name))
        obj = super().destroy(request, *args, **kwargs)
        return obj
