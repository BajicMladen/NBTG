from rest_framework import serializers

from .models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "date_joined",
            "email",
            "display_name",
        ]
