from django.contrib import admin

from .models import Drone, DroneTest, Order

admin.site.register(Drone)
admin.site.register(DroneTest)
admin.site.register(Order)
