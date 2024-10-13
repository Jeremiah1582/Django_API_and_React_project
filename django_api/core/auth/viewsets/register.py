from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from core.auth.serializers.register import RegistrationSerializer

class RegisterViewSet(ViewSet): 
    serializer_class= RegistrationSerializer
    permission_classes = (AllowAny,)
    http_method_names= ['post']
    
    def create(self, request, *args, **kwargs): 
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(): 
            user = serializer.save()
            refresh= RefreshToken.for_user(user)
            res={
                "refresh":str(refresh), 
                "access": str(refresh.access_token),            
            }
            return Response({
                "User": serializer.data, 
                "refresh": res["refresh"],
                "token": res["access"],
            }, status=status.HTTP_201_CREATED)
        
        else: 
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )