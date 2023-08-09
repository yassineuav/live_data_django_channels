from rest_framework import serializers

from .models import Drone, DroneTest, Order, OrderStatus, Coordinates, OrderHistoryStatus


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


class HistoryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderHistoryStatus
        fields = '__all__'
        # depth = 1


class OrderSerializer(serializers.ModelSerializer):
    # update_status = HistoryStatusSerializer(read_only=True)
    status_history = HistoryStatusSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        # fields = '__all__'
        fields = ['id', 'weight', 'description', 'updated_at', 'status', 'status_history']
        depth = 1



