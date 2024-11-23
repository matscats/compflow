from rest_framework import permissions


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_student


class IsOwnerOfHistory(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
