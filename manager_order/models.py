from django.db import models


class Status(models.Model):
    status = models.CharField(max_length=200, unique=True)
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
    status = models.OneToOneField(Status, on_delete=models.CASCADE)
