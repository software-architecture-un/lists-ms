from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueTogetherValidator
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListPlace
        fields = '__all__'

class ListWhitPlacesSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, read_only=True)
    class Meta:
        model = List
        fields = ('id','id_user','name', 'comment', 'estimatedDate', 'places')