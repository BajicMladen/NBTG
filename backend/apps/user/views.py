from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from .models import User
from .serializers import UserDetailSerializer


class UserViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserDetailSerializer

    @action(
        detail=False,
        methods=["get"],
        url_path="current-user",
        permission_classes=[permissions.IsAuthenticated],
    )
    def get_current_user(self, request: Request):
        return Response(
            data=UserDetailSerializer(request.user).data,
            status=status.HTTP_200_OK,
        )
