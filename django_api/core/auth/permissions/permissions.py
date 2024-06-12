from rest_framework.permissions import BasePermission, SAFE_METHODS

class UserPermission(BasePermission):
    
    def has_object_permission(self, request, view, obj):         
        '''if anonymous user, only grant access to safe_methods. authenticated user have access to unsafe http methods'''
               
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS
        if view.basename in ['post', 'put']: #
            return bool(request.user and request.user.is_authenticated)
        return False
   
    def has_permission(self,request,view):
        '''if authenticated then authorize access to unsafe http methods, i.e. post, patch'''
        
        if view.basename in ['post', 'put']:
            if request.user.is_anonymous:
                return request.method in SAFE_METHODS
            return bool(request.user and request.user.is_authenticated)
        return False