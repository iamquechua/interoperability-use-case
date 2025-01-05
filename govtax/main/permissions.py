from rest_framework.permissions import BasePermission


class IsAccessedThroughKong(BasePermission):
   def has_permission(self, request, view):
       allowed_hosts = ['host.docker.internal:8010']
       if request.get_host() not in allowed_hosts:
           return False
       return True