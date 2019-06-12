from django.shortcuts import render
from .models import *
from .serealizers import *
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route,api_view

@api_view(['GET'])
def lists_by_user(request,pk):
    queryset = List.objects.filter(id_user=pk)
    serializer = ListSerializer(queryset,many=True)
    response = buildResponse(serializer.data, '') 
    return Response(response)

@api_view(['GET'])
def list_with_places_by_list(request,pk):
    queryset = List.objects.filter(id=pk)
    serializer = ListWhitPlacesSerializer(queryset,many=True)
    response = buildResponse(serializer.data, '') 
    return Response(response)


@api_view(['GET'])
def places_by_list(request,pk):
    queryset = ListPlace.objects.filter(id_list=pk)
    serializer = PlaceSerializer(queryset,many=True)
    response = buildResponse(serializer.data, '') 
    return Response(response)

@api_view(['GET', 'PUT', 'DELETE'])
def place(request,pk):
    try:
        place = ListPlace.objects.filter(id=pk)
    except ListPlace.DoesNotExist: 
        return Response(buildResponse(place, ''),status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlaceSerializer(place,many=True)
        response = buildResponse(serializer.data, '') 
        return Response(response)
    elif request.method == 'PUT':
        serializer = PlaceSerializer(place.first(),data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = buildResponse(serializer.data, 'Place was update') 
            return Response(response)
        return Response(buildResponse(None,serializer.errors), status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        place.delete()
        return Response(buildResponse(None,'Place was delete'),status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def place_create(request):
    serializer = PlaceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = buildResponse(serializer.data, 'Place was created') 
        return Response(response, status=status.HTTP_201_CREATED)
    return Response(buildResponse(None,serializer.errors), status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def lists(request,pk):
    try:
        listObj = List.objects.filter(id=pk)
    except List.DoesNotExist: 
        return Response(buildResponse(listObj, ''),status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ListSerializer(listObj,many=True)
        response = buildResponse(serializer.data, '') 
        return Response(response)
    elif request.method == 'PUT':
        serializer = ListSerializer(listObj.first(),data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = buildResponse(serializer.data, 'List was update') 
            return Response(response)
        return Response(buildResponse(None,serializer.errors), status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        listObj.delete()
        return Response(buildResponse(None,'List was delete'),status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def lists_create(request):
    serializer = ListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = buildResponse(serializer.data, 'List was created') 
        return Response(response, status=status.HTTP_201_CREATED)
    return Response(buildResponse(None,serializer.errors), status=status.HTTP_400_BAD_REQUEST)

def buildResponse(data, message):
    response = {'content':{}, 'message': message}
    if not (data is None):
        response['content'] = data
    return response

