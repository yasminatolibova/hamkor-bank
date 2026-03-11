from ..accounts.serializers import UserSerializer
from .models import QrCode
from rest_framework import serializers

class QrCodeSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model= QrCode
        fields=['id', 'user', 'account', 'status', 'type', 'qr_code', 'qr_uuid', 'created_at', 'expire_date', 'data' ]
        read_only_fields=['created_at']