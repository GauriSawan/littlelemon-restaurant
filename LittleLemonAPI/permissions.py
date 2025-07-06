from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='manager').exists()

class IsDeliveryCrew(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='delivery_crew').exists()
