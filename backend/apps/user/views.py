from django.contrib.auth.models import Group
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserDetailSerializer, UserWriteSerializer


class UserViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ["username"]
    search_fields = ["username", "first_name", "last_name", "email"]
    ordering_fields = ["username", "first_name", "last_name"]

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


class SignInViewSet(APIView):
    permission_classes = [permissions.AllowAny]
    http_method_names = ["post", "head"]

    def post(self, request, format=None):
        serializer = UserWriteSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.groups.add(Group.objects.get(name="Customer"))
            user.save()

        return Response(
            data=UserDetailSerializer(user).data,
            status=status.HTTP_200_OK,
        )
