from rest_framework import viewsets
from ..models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

########################## VIEWSET ##########################

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



########################## GENERICS ##########################
#################### NÃO ESTÁ SENDO USADA ####################

#List and create
class RegisterListCreateGenerics(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer()
    permission_classes = (AllowAny,)
    #permission_classes = [IsAdminUser]

#List
class RegisterListGenerics(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Create
class RegisterCreateGenerics(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



