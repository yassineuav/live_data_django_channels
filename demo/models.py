from MySQLdb.constants.FIELD_TYPE import NULL
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
    latitude = models.DecimalField(max_digits=20, decimal_places=10)
    longitude = models.DecimalField(max_digits=20, decimal_places=10)


class Drone(models.Model):
    name = models.CharField(max_length=200)
    weight = models.IntegerField(default=1)
    distance = models.IntegerField(default=1)
    status = models.CharField(max_length=25, default="off")
    # DroneStatus = models.OneToOneField(DroneStatus, on_delete=models.CASCADE)
    # coordinates = models.OneToOneField(Coordinates, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=20, decimal_places=7, default="37.5566056")
    longitude = models.DecimalField(max_digits=20, decimal_places=7, default="-122.0287363")
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


# hint
class OrderStatus(models.Model):
    status = models.CharField(max_length=250, default="pending")
    updated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    departure_address = models.CharField(max_length=200, default="36039 Pizarro dr, Fremont, Ca, 94653")
    departure_latitude = models.DecimalField(max_digits=20, decimal_places=7, default="37.5566056")
    departure_longitude = models.DecimalField(max_digits=20, decimal_places=7, default="-122.0287363")
    landing_address = models.CharField(max_length=200, default="35820 Fremont Blvd, Fremont, CA 94536")
    landing_latitude = models.DecimalField(max_digits=20, decimal_places=7, default="37.5605321")
    landing_longitude = models.DecimalField(max_digits=20, decimal_places=7, default="-122.0180234")
    order_description = models.TextField(default="no description")
    description = models.TextField(default="no description")
    weight = models.IntegerField(default=10)
    trigger = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=250, default="pending")
    status_id = models.SmallIntegerField(default=1)
    # update_status = models.ForeignKey(OrderHistoryStatus, related_name='update_status', default=get_default_status,
    # on_delete=models.CASCADE, blank=True, null=True)


class OrderHistory(models.Model):
    status = models.CharField(max_length=250, default="pending")
    status_id = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(default="no description")
    comment = models.TextField(default="no comment")
    updated_from = models.CharField(max_length=200, default="programmer")
    order_history = models.ForeignKey(Order, on_delete=models.CASCADE)


def get_default_status():
    default_status, _ = OrderHistory.objects.get_or_create(status='pending')
    return default_status

