from django.shortcuts import render
from rest_framework import viewsets

from .models import Drone, DroneTest, Order, OrderHistoryStatus, OrderStatus, Coordinates
from .serializers import DroneTestSerializer, DroneSerializer, HistoryStatusSerializer, StatusSerializer, OrderSerializer, CoordinatesSerializer


class DroneViewSet(viewsets.ModelViewSet):
    serializer_class = DroneSerializer
    queryset = Drone.objects.all()


class DroneTestViewSet(viewsets.ModelViewSet):
    serializer_class = DroneTestSerializer
    queryset = DroneTest.objects.all()


class CoordinatesViewSet(viewsets.ModelViewSet):
    serializer_class = CoordinatesSerializer
    queryset = Coordinates.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    # queryset = Order.objects.all()


class OrderStatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = OrderStatus.objects.all()


class OrderHistoryStatusViewSet(viewsets.ModelViewSet):
    serializer_class = HistoryStatusSerializer
    queryset = OrderHistoryStatus.objects.all()


def index(request):
    return render(request, "demo/index.html")
