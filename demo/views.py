from django.shortcuts import render
from rest_framework import viewsets

from .models import Drone, DroneTest
from .serializers import DroneTestSerializer, DroneSerializer


class DroneViewSet(viewsets.ModelViewSet):
    serializer_class = DroneSerializer
    queryset = Drone.objects.all()


class DroneTestViewSet(viewsets.ModelViewSet):
    serializer_class = DroneTestSerializer
    queryset = DroneTest.objects.all()


def index(request):
    return render(request, "demo/index.html")
