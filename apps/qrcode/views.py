from django.shortcuts import render
from .models import QrCode
from .serializers import QrCodeSerializer
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrAdmin


class QrcodeListCreate(generics.ListCreateAPIView):
    serializer_class=QrCodeSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return QrCode.objects.filter(user=self.request.user)
        

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class QrcodeRetrieveDestroy(generics.RetrieveDestroyAPIView):
    
    serializer_class=QrCodeSerializer
    permission_classes=[permissions.IsAuthenticated, IsOwnerOrAdmin]
    lookup_field= 'id'

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return QrCode.objects.none()

        return QrCode.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)