from rest_framework import viewsets
from rest_framework import filters

# Create your views here.
class AbstractViewSet(viewsets.ModelViewSet):
    filter_backends =[filters.OrderingFilter]   #This sets the default filter backend
    ordering_fields =['updated', 'created']      #This list contains the fields that can be used as ordering parameters when making a request
    ordering=['-updated']                       #This will tell Django REST in which order to send many objects as a response. In this case, all the responses will be ordered by the most recently updated.