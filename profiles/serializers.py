from rest_framework import serializers
from .models import CustomerProfile, TechnicianProfile
from django.contrib.auth.models import User

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")

class CustomerProfileSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)

    class Meta:
        model = CustomerProfile
        fields = ("id", "user", "user_id", "address", "contact_phone")

class TechnicianProfileSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)

    class Meta:
        model = TechnicianProfile
        fields = (
            "id",
            "user",
            "user_id",
            "specialization",
            "availability",
            "latitude",
            "longitude",
        )
