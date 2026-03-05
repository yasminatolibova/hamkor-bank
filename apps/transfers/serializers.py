from ..accounts.serializers import UserSerializer
from .models import Transaction, Transfer
from rest_framework import serializers

class TransferSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Transfer
        fields=['id', 'user', 'from_account', 'to_account', 'amount', 'status', 'created_at']
        read_only_fields=['created_at']

class TransactionSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Transaction
        fields=['id', 'user', 'amount', 'account', 'type', 'description', 'created_at']   