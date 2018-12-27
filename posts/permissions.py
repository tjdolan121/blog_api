from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Overrides BasePermission's has_object_permission
    to limit write access to the original author only."""

    def has_object_permission(self, request, view, obj):
        # Read-Only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user
