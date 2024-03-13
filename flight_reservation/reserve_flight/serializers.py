from rest_framework import serializers
from .models import flightModel, passengerModel, reservationModel
import re 
class flightSerializer(serializers.ModelSerializer):
    class Meta:
        model = flightModel
        fields = "__all__"

    def validate_flightNumber(self, flightNumber):
        if re.match("^[a-zA-Z0-9]*$",flightNumber) == None:
            raise serializers.ValidationError("Invalid flightNumber")
        return flightNumber

class reservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = reservationModel
        fields = "__all__"


class passengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = passengerModel
        fields = "__all__"