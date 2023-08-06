from rest_framework import serializers

from .models import Drone, DroneTest, Order, OrderStatus, Coordinates


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = "__all__"


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = "__all__"


class DroneTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = DroneTest
        # fields = ['id', 'status', 'name', 'battery']
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'weight', 'updated_at', 'status', 'status_description']


