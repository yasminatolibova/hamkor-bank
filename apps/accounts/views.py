from django.shortcuts import render
from rest_framework import generics, status, permissions
from .models import User, Accounts
from .serializers import UserSerializer, AccountSerializer, RegisterSerializer, ResetPasswordSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAuthenticated



class RegisterCreateAPI(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  
        return Response({
            'user': UserSerializer(user).data,
            'message': 'Muvaffaqiyatli ruyxatdan utildi'
        }, status=status.HTTP_201_CREATED)

class LoginThrottle(UserRateThrottle):
    rate='10/min'

class LoginView(ObtainAuthToken):
    throttle_classes=[LoginThrottle]
    
    def post(self, request, *args, **kwargs):
        response=super().post(request, *args, **kwargs)
        return Response({'token':response.data['token']})
    

class LogoutView(generics.UpdateAPIView):
    def get_serializer(self):
        return None
    
class ResetPassword(generics.UpdateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ResetPasswordSerializer

    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        user=self.get_object()
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        update_ses_auth_hash(request, user)
        return Response({'message':'Password updated'}, status=status.HTTP_200_OK)
    

class OwnProfileView(generics.RetrieveAPIView):
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]

    def get_object(self):
        return self.request.user

class ProfileListView(generics.ListAPIView):
    permission_classes=[permissions.IsAdminUser]
    serializer_class=UserSerializer
    queryset=User.objects.all()

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAdminUser]
    queryset=User.objects.all()
    lookup_field='id'

class AccountListView(generics.ListAPIView):
    queryset=Accounts.objects.all()
    permission_classes=[permissions.IsAdminUser]
    serializer_class=AccountSerializer
    lookup_field='id'


