from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScheduleViewSet

router = DefaultRouter()
router.register(r"", ScheduleViewSet, basename="schedule")

urlpatterns = [
    path("schedule/", include(router.urls)),
]
