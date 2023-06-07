from rest_framework import serializers

from .models import User


class UserDetailSerializer(serializers.ModelSerializer):
    is_admin = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "date_joined", "email", "image", "is_admin"]

    def get_is_admin(self, instance):
        return instance.groups.filter(name="Admin").exists()

class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password", "image"]