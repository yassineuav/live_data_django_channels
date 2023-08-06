from django.contrib.auth.models import User
from django.db import models

STATUS = (
    (0, "OFF"),
    (1, "ON"),
    (2, "Starting"),
    (3, "Pending"),
    (4, "shutting off")
)


class DroneStatus(models.Model):
    status = models.CharField(max_length=200, unique=True)
    brief = models.CharField(max_length=500)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Drone(models.Model):
    name = models.CharField(max_length=200)
    weight = models.IntegerField(default=1)
    distance = models.IntegerField(default=1)
    status = models.IntegerField(choices=STATUS, default=0)
    # DroneStatus = models.OneToOneField(DroneStatus, on_delete=models.CASCADE)
    battery = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DroneTest(models.Model):
    name = models.CharField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    battery = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# system controller model history