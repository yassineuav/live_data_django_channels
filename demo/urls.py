
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register("coordinates", views.CoordinatesViewSet, basename="coordinates")
router.register("drone", views.DroneViewSet, basename="drone")
router.register("dronetest", views.DroneTestViewSet, basename="dronetest")

router.register("order", views.OrderViewSet, basename="order")
router.register("order_status", views.OrderStatusViewSet, basename="order_status")
router.register("order_histoy_status", views.OrderHistoryStatusViewSet , basename="order_histoy_status")

urlpatterns = [
    path("", views.index,)
]

urlpatterns += router.urls
