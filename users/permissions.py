from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class IsAdminOwner(permissions.BasePermission):
    def has_object_permission(self, req: Request, view: View, obj: User):
        return req.user.is_employee or obj == req.user
