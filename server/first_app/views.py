from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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
