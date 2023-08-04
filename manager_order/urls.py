from django.urls import path
from rest_framework.routers import DefaultRouter

from manager_order import views

router = DefaultRouter()

router.register("order", views.OrderViewSet, basename="order")
router.register("status", views.StatusViewSet, basename="status")

# urlpatterns = [
#     path("order", views.index,)
# ]
#
urlpatterns = []
urlpatterns += router.urls
