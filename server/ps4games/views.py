from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ps4games import models
from ps4games import serializers


@api_view(['POST', 'GET'])
def add_game(request):
    data = {
        'name': request.data['name'],
        'release': request.data['release'],
        'metacritic': request.data['metacritic'],
        'gptime': request.data['gptime'],
        'image': request.data['image']
    }

    ser = serializers.PS4GameSerializer(data=data)
    if ser.is_valid():
        print("1: before api_view_save")
        ser.save()
        print("4: after api_view_save")
        return Response(data=ser.data, status=status.HTTP_201_CREATED)
    else:
        print("api_view_err")
        return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
def get_games(request):
    games = models.PS4Game.objects.all()
    ser = serializers.PS4GameSerializer(games, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)


@api_view(['POST', 'PUT', 'DELETE'])
def up_del_get_game(request, pk):
    try:
        ps4game = models.PS4Game.objects.get(pk=pk)
        if request.method == 'POST':
            ser = serializers.PS4GameSerializer(ps4game)
            return Response(ser.data, status=status.HTTP_200_OK)

        elif request.method == 'DELETE':
            ps4game.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        elif request.method == 'PUT':
            ser = serializers.PS4GameSerializer(ps4game, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=status.HTTP_200_OK)
            else:
                return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    except:
        return Response({"message": "Game not found!"})


@api_view(['GET'])
def search_game(request):
    games = models.PS4Game.objects.filter(name=request.query_params['name'])
    if games:
        ser = serializers.PS4GameSerializer(games, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)














