from rest_framework.permissions import BasePermission

class IsPrincipalTask(BasePermission):
    """
    Return `True` if permission is granted, `False` otherwise.
    """
    def has_object_permission(self, request, view, obj):

        return obj.taskAssignedby == request.user
    
class IsProxyTask(BasePermission):
    """
    Return `True` if permission is granted, `False` otherwise.
    """
    def has_object_permission(self, request, view, obj):

        return obj.taskCarriedBy == request.user