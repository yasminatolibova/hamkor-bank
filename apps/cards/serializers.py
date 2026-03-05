from .models import Card
from ..accounts.models import User
from rest_framework import serializers
from ..accounts.serializers import UserSerializer


class CardSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Card
        fields=['id', 'balance', 'user', 'is_blocked', 'expire_date', 'created_at', 'card_number']
        read_only_fields=['created_at', 'expire_date']
