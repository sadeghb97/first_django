from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from .permissions import IsOwner
from .serializers import ProfileUserSerializer


@api_view(['POST'])
@permission_classes((AllowAny, ))
def register_user(request):
    ser = ProfileUserSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated, IsOwner))
def get_profile(request):
    try:
        user = User.objects.get(username=request.query_params['username'])
        ser = ProfileUserSerializer(user)
        return Response(ser.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


