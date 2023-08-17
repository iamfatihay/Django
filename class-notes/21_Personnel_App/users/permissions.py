from rest_framework.permissions import BasePermission

class IsOwnerOrStaff(BasePermission):
    