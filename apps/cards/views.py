from django.shortcuts import render
from .serializers import CardSerializer
from .models import Card
from rest_framework import status, generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAuthenticated
from .permisions import IsOwnerOrAdmin


class CardCreateView(generics.CreateAPIView):
    queryset=Card.objects.all()
    serializer_class=CardSerializer
    permission_classes=[IsAuthenticated, IsOwnerOrAdmin]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CardListView(generics.ListAPIView):
    queryset=Card.objects.all()
    serializer_class=CardSerializer
    permission_classes=[permissions.IsAdminUser]
