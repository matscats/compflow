from rest_framework import viewsets, status, permissions, views
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from .serializers import HistorySerializer
from .models import History
from .permissions import IsStudent, IsOwnerOfHistory

User = get_user_model()


class HistoryViewSet(viewsets.ModelViewSet):
    serializer_class = HistorySerializer
    permission_classes = [IsAuthenticated, IsStudent]

    def get_permissions(self):
        permissions = super().get_permissions()

        if self.action in ["retrieve", "update", "partial_update", "destroy"]:
            permissions.append(IsOwnerOfHistory())

        return permissions

    def get_queryset(self):
        user = self.request.user
        return History.objects.filter(user=user)
