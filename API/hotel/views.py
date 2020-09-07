from django.shortcuts import render
from hotel.serializers import  HotelSerializer
from rest_framework import viewsets
from hotel.models import Hotel
# Create your views here.

class HotelModelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
