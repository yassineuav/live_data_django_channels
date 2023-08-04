from rest_framework import serializers

from .models import Drone, DroneTest, STATUS


class DroneSerializer(serializers.ModelSerializer):

    # author = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Drone
        fields = "__all__"

    def get_status(self, obj):
        return STATUS[obj.status][1]


class StatusField(serializers.ChoiceField):
    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        return next(key for key, value in self._choices.items() if value == data)


class DroneTestSerializer(serializers.ModelSerializer):
    # author = serializers.SerializerMethodField()
    # status = serializers.SerializerMethodField()
    STATUS_CHOICES = (
        (0, "OFF"),
        (1, "ON"),
        (2, "Starting"),
        (3, "Pending"),
        (4, "shutting off")
    )

    status = serializers.ChoiceField(choices=STATUS_CHOICES)
    # status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return self.STATUS_CHOICES[obj.status][1]

    class Meta:
        model = DroneTest
        fields = ['id', 'status', 'name', 'battery']
        # fields = '__all__'
