from rest_framework import permissions


class UserDetailPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Read only(GET, HEAD, OPTIONS) for all users
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write only(POST, PATCH, PUT) for admin. superuser and me
        if request.method in ('POST', 'PATCH', 'PUT'):
            return request.user and request.user.roles.filter(name='Admin').exists() or\
                request.user.is_superuser or\
                request.user.id == view.kwargs['id']
        # Delete only for superusers
        return request.user and request.user.is_superuser


class IsAdminOrSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.roles.filter(name='Admin').exists() or\
            request.user.is_superuser



