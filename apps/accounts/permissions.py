from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
   def  has_object_permission(self, request, view, obj):
      return request.user.role == 'admin' or obj.user == request.user
   
