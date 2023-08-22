from rest_framework.permissions import BasePermission, SAFE_METHODS
# from rest_framework import permissions


# class IsOwnerOrStaff(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return bool(request.user.is_staff or (request.user == obj.user))


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  #! GET
            return True                     #! unsafe  PUT, POST
        else:
            return bool(request.user.is_staff)