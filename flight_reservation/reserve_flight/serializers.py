from rest_framework import serializers
from .models import flightModel, passengerModel, reservationModel

class flightSerializer(serializers.ModelSerializer):
    class Meta:
        model = flightModel
        fields = "__all__"


class passengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = passengerModel
        fields = "__all__"

class reservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = reservationModel
        fields = "__all__"