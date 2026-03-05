from django.shortcuts import render
from .models import Transfer, Transaction
from rest_framework import status, generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .serializers import TransactionSerializer, TransferSerializer
from rest_framework.exceptions import ValidationError
from django.db import transaction

class TransferCreateView(generics.CreateAPIView):
    queryset=Transfer.objects.all()
    serializer_class=TransferSerializer
    permission_classes=[permissions.IsAuthenticated]

    @transaction.atomic()
    def perform_create(self, serializer):
        
        from_account=serializer.validated_data['sender']
        to_account=serializer.validated_data['receiver']
        amount=serializer.validated_data['amount']

        if from_account.balance<amount:
            raise ValidationError('insufficient balance')
        from_account.balance-=amount
        to_account.balance+=amount
        from_account.save()
        to_account.save()
        serializer.save()

class TransferListView(generics.ListAPIView):
    queryset=Transfer.objects.all()
    serializer_class=TransferSerializer
    permission_classes=[IsOwnerOrReadOnly]


class TransactionList(generics.ListAPIView):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer
    permission_classes=[permissions.IsAuthenticated]
    