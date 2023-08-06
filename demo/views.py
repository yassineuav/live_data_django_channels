from django.shortcuts import render
from rest_framework import viewsets

from .models import Drone, DroneTest, Order, OrderStatus
from .serializers import DroneTestSerializer, DroneSerializer, StatusSerializer, OrderSerializer


class DroneViewSet(viewsets.ModelViewSet):
    serializer_class = DroneSerializer
    queryset = Drone.objects.all()


class DroneTestViewSet(viewsets.ModelViewSet):
    serializer_class = DroneTestSerializer
    queryset = DroneTest.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderStatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = OrderStatus.objects.all()


def index(request):
    return render(request, "demo/index.html")
