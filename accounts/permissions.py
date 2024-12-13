from rest_framework import permissions


# class isUser(permissions.BasePermission):
#     message = 'Adding satients not allowed.'
#
#     def has_permission(self, request, view):
#             if request.user is what I want:
#                 return True
#             else:
#                 return False


class ReadOnly(permissions.BasePermission):
    message = 'Adding satients not allowed.'
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
