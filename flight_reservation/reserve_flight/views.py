from django.shortcuts import render
from .models import flightModel,passengerModel,reservationModel
from .serializers import flightSerializer,passengerSerializer,reservationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class flights(APIView):
    def get(self, request):
        flightsData = flightModel.objects.all()
        flightsSerlizr = flightSerializer(flightsData, many=True)
        
        return Response(flightsSerlizr.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        flightsSerlizr = flightSerializer( data=request.data)
        if flightsSerlizr.is_valid():
            flightsSerlizr.save()
            return Response(flightsSerlizr.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class fight(APIView):
    def get(self, request, pk):
        try:

