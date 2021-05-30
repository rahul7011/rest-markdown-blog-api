from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsAuthor(permissions.BasePermission):
    # this is the default function of basepermissions class
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user