from django.contrib.auth.models import Group
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserDetailSerializer, UserWriteSerializer


def isAdmin(user):
    return user.groups.filter(name="Admin").exists()


class UserViewset(viewsets.ModelViewSet):
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ["username"]
    search_fields = ["username", "first_name", "last_name", "email"]
    ordering_fields = ["username", "first_name", "last_name"]

    def get_queryset(self):
        if isAdmin(self.request.user):
            return User.objects.all()
        else:
            return User.objects.filter(id=self.request.user.id)

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
    
    @action(
        detail=False,
        methods=["patch"],
        url_path="update_info",
        permission_classes=[permissions.IsAuthenticated],
    )
    def update_info(self, request: Request):
        print(request.user)

        data = {
            "first_name": request.data['firstName'],
            "last_name": request.data['lastName'],
            "username": request.data['username']
        }

        User.objects.filter(id = request.user.id).update(**data)
        # request.user.update(**data)

        return Response(
            data=UserDetailSerializer(User.objects.get(id = request.user.id)).data,
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
            user.set_password(user.password)
            user.save()

        return Response(
            data=UserDetailSerializer(user).data,
            status=status.HTTP_200_OK,
        )
