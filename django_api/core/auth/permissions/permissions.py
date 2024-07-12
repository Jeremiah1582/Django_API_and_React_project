from rest_framework.permissions import BasePermission, SAFE_METHODS

class UserPermission(BasePermission):
    
    def has_object_permission(self, request, view, obj):         
        '''if anonymous user, only grant access to safe_methods. authenticated user have access to unsafe http methods'''
       

        # Only allow anonymous Users to access safe methods
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS
        
        # only allow authenticated user to access put and post request
        if view.basename in [ 'post']: #
            return bool(request.user and request.user.is_authenticated)
        # Delete Permission--authenticated authors or superusers can delete
        if view.basename in ["post-comment"]:
            if request.method in ["DELETE"]: 
                return bool(request.user.is_superuser or request.user in [obj.author, obj.post.author]) 
            return bool(request.user and request.user.is_authenticated)
        
        return False
    
       
   
    def has_permission(self,request,view):
        '''if authenticated then authorize access to unsafe http methods, i.e. post, patch'''
        
        if view.basename in ['post', 'post-comment']:
            if request.user.is_anonymous:
                return request.method in SAFE_METHODS
            return bool(request.user and request.user.is_authenticated)
        return False