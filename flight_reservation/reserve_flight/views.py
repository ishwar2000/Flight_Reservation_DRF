from django.shortcuts import render
from django.http import Http404

from .models import flightModel,passengerModel,reservationModel
from .serializers import flightSerializer,passengerSerializer,reservationSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(["POST"])
def find_flight(request):
    data = flightModel.objects.all()
    
    if "DepartureCity" in request.data:
        data = data.filter(
            DepartureCity = request.data["DepartureCity"]
            
        )

    if "arrivalCity" in request.data:
        data = data.filter(
            arrivalCity = request.data["arrivalCity"]
            
        )

    serlizData = flightSerializer(data, many=True)
    return Response(serlizData.data)

@api_view(["POST"])
def reserveFlight(request):
    flightData = flightModel.objects.get(id=request.data["flightNumber"])

    passenger = passengerModel.objects.get(id=request.data["passegerID"])

    reserv = reservationModel()
    reserv.flight = flightData
    reserv.passenger = passenger

    reservationModel.save(reserv)

    reservSrlz = reservationSerializer(reserv)

    return Response(reservSrlz.data,status=status.HTTP_201_CREATED)

class flights(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        flightsData = flightModel.objects.all()
        flightsSerlizr = flightSerializer(flightsData, many=True)
        
        return Response(flightsSerlizr.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        flightsSerlizr = flightSerializer( data=request.data)
        if flightsSerlizr.is_valid():
            flightsSerlizr.save()
            return Response(flightsSerlizr.data, status=status.HTTP_201_CREATED)
        return Response(flightsSerlizr.errors,status=status.HTTP_400_BAD_REQUEST)

class flight(APIView):
    def get_object(self, request, pk):
        try:
            data = flightModel.objects.get(id=pk)
            return data
        except flightModel.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        flightData = self.get_object(request, pk)
        serilzData = flightSerializer(flightData)
        return Response(serilzData.data)
    
    def put(self, request, pk):
        flightData = self.get_object(request, pk)
        serilzData = flightSerializer(flightData, data=request.data)

        if serilzData.is_valid() :
            serilzData.save()
            return Response(serilzData.data, status=status.HTTP_200_OK)
        return Response(serilzData.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        flightData = self.get_object(request, pk)
        serilzData = flightSerializer(flightData, data=request.data, partial=True)

        if serilzData.is_valid() :
            serilzData.save()
            return Response(serilzData.data, status=status.HTTP_200_OK)
        return Response(serilzData.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        flightData = self.get_object(request, pk)
        

        if flightData.is_valid() :
            flightData.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(flightData.errors, status=status.HTTP_400_BAD_REQUEST)

class passengers(APIView):
    def get(self, request):
        passData = passengerModel.objects.all()
        passSerlizr = passengerSerializer(passData, many=True)
        
        return Response(passSerlizr.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        passSerlizr = passengerSerializer( data=request.data)
        if passSerlizr.is_valid():
            passSerlizr.save()
            return Response(passSerlizr.data, status=status.HTTP_201_CREATED)
        return Response(passSerlizr.errors,status=status.HTTP_400_BAD_REQUEST)

class passenger(APIView):
    def get_object(self, request, pk):
        try:
            data = passengerModel.objects.get(id=pk)
            return data
        except passengerModel.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        passData = self.get_object(request, pk)
        serilzData = passengerModel(passData)
        return Response(serilzData.data)
    
    def put(self, request, pk):
        passData = self.get_object(request, pk)
        serilzData = passengerSerializer(passData, data=request.data)

        if serilzData.is_valid() :
            serilzData.save()
            return Response(serilzData.data, status=status.HTTP_200_OK)
        return Response(serilzData.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        passData = self.get_object(request, pk)
        serilzData = flightSerializer(passData, data=request.data, partial=True)

        if serilzData.is_valid() :
            serilzData.save()
            return Response(serilzData.data, status=status.HTTP_200_OK)
        return Response(serilzData.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        flightData = self.get_object(request, pk)
        

        if flightData.is_valid() :
            flightData.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(flightData.errors, status=status.HTTP_400_BAD_REQUEST)

class reservations(APIView):
    def get(self, request):
        reservData = reservationModel.objects.all()
        reservSerlizr = reservationSerializer(reservData, many=True)
        
        return Response(reservSerlizr.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        reservSerlizr = reservationSerializer( data=request.data)
        if reservSerlizr.is_valid():
            reservSerlizr.save()
            return Response(reservSerlizr.data, status=status.HTTP_201_CREATED)
        return Response(reservSerlizr.errors,status=status.HTTP_400_BAD_REQUEST)

class reservation(APIView):
    def get_object(self, request, pk):
        try:
            data = reservationModel.objects.get(id=pk)
            return data
        except reservationModel.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        reservData = self.get_object(request, pk)
        serilzData = reservationSerializer(reservData)
        return Response(serilzData.data)
    
    def put(self, request, pk):
        reservData = self.get_object(request, pk)
        serilzData = reservationSerializer(reservData, data=request.data)

        if serilzData.is_valid() :
            serilzData.save()
            return Response(serilzData.data, status=status.HTTP_200_OK)
        return Response(serilzData.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        reservData = self.get_object(request, pk)
        serilzData = reservationSerializer(reservData, data=request.data, partial=True)

        if serilzData.is_valid() :
            serilzData.save()
            return Response(serilzData.data, status=status.HTTP_200_OK)
        return Response(serilzData.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reservData = self.get_object(request, pk)
        

        if reservData.is_valid() :
            reservData.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(reservData.errors, status=status.HTTP_400_BAD_REQUEST)

