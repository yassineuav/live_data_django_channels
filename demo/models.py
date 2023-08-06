from django.contrib.auth.models import User
from django.db import models

# STATUS = (
#     (0, "OFF"),
#     (1, "ON"),
#     (2, "Starting"),
#     (3, "Pending"),
#     (4, "shutting off")
# )


class DroneStatus(models.Model):
    status = models.CharField(max_length=200, unique=True)
    brief = models.CharField(max_length=500)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Coordinates(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)


class Drone(models.Model):
    name = models.CharField(max_length=200)
    weight = models.IntegerField(default=1)
    distance = models.IntegerField(default=1)
    status = models.CharField(max_length=25, default="OFF")
    # DroneStatus = models.OneToOneField(DroneStatus, on_delete=models.CASCADE)
    coordinates = models.OneToOneField(Coordinates, on_delete=models.CASCADE)
    battery = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DroneTest(models.Model):
    name = models.CharField(max_length=200, unique=True)
    status = models.CharField(max_length=200, default="OFF")
    battery = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class SystemHistory(models.Model):
    command = models.CharField(max_length=250, unique=True)
    brief = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderStatus(models.Model):
    status = models.CharField(max_length=250, unique=True)
    # brief = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    from_address = models.CharField(max_length=200, unique=True)
    to_address = models.CharField(max_length=200, unique=True)
    # from_location = models.PointField(geography=True, default=Point(0.0, 0.0))
    from_location_lat = models.DecimalField(max_digits=9, decimal_places=6)
    from_location_lon = models.DecimalField(max_digits=9, decimal_places=6)
    to_location_lat = models.DecimalField(max_digits=9, decimal_places=6)
    to_location_lon = models.DecimalField(max_digits=9, decimal_places=6)
    describe = models.TextField()
    weight = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.OneToOneField(OrderStatus, on_delete=models.CASCADE)