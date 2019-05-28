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
    # id = serializers.IntegerField(read_only=True)
    # id_list = serializers.IntegerField(read_only=True)
    # placeLon = serializers.FloatField(required=False)
    # placeLat = serializers.FloatField(required=False)

    # def update(self, instance, validated_data):
    #     instance.placeLat = validated_data.get('placeLat', instance.placeLat)
    #     instance.placeLon = validated_data.get('placeLon', instance.placeLon)
    #     instance.save()
    #     return instance

    class Meta:
        model = ListPlace
        fields = ('placeLat','placeLon','id_list', 'id')

class ListWhitPlacesSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, read_only=True)
    class Meta:
        model = List
        fields = ('id','id_list','name', 'comment', 'estimatedDate', 'order', 'places')