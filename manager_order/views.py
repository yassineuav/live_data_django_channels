from rest_framework import viewsets
from manager_order.models import Order, Status
from manager_order.serializers import OrderSerializer, StatusSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class StatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
