from rest_framework import serializers
from hotel.models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id','latitude','longitude','service_type')