from rest_framework.permissions import BasePermission

class CustomUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_staff
        elif request.method == 'POST':
            return request.user.is_authenticated
      
class CustomUserDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_authenticated
        elif request.method == 'PUT':
            return request.user.is_authenticated
        elif request.method == 'DELETE':
            return request.user.is_authenticated

class ProductPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST':
            return request.user.is_authenticated
      
class ProductDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'PUT':
            return request.user.is_authenticated
        elif request.method == 'DELETE':
            return request.user.is_authenticated
        
class RubricPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_staff
        if request.method == 'POST':
            return request.user.is_staff
                
class RubricDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_staff
        if request.method == 'PUT':
            return request.user.is_staff
        if request.method == 'DELETE':
            return request.user.is_staff
