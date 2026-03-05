from .models import User, Accounts, ID_CARD
from rest_framework import serializers

class IdcardSerializer(serializers.ModelSerializer):
    class Meta:
        model=ID_CARD
        fields=['full_name', 'date_of_birth', 'personal_number']
        read_only_fields=['personal_number']

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id', 'username', 'email', 'address',
        'phone', 'full_name', 'passport', 'created_at', 'password']
        read_only_fields=['username', 'created_at']
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username', 'password', 'email']
    

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class ResetPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError("Incorrect old password.")
        return value
    

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Accounts
        fields=['id', 'user', 'currency', 'account_number', 'balance' ]
        read_only_fields=['account_number']
