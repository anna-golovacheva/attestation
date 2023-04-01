import datetime

from rest_framework import permissions


class PostOrCommentUpdatePermissionManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user == view.get_object().author:
            return True
        return False


class PostAppropriateAgePermissionManager(permissions.BasePermission):
    def has_permission(self, request, view):
        now = datetime.datetime.today()
        birth = request.user.date_of_birth
        return (
                now.year - birth.year > 18
                or now.year - birth.year == 18 and (
                        now.month > birth.month
                        or now.month == birth.month and now.day >= birth.day
                )
        )

