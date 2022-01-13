from rest_framework.permissions import BasePermission


class IsProjectContributor(BasePermission):

    def has_permission(self, request, view):
        print(self.__dict__)
        print(request.user)
        print(view.__dict__)
        return bool(request.user and request.user.is_authenticated)

    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            print(self)
            print(request)
            print(view)
            print(obj)
            return True
    """

