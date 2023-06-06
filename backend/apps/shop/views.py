from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Brand, Category, Game, Order, OrderItem, Review, ShippingAddress
from .pagination import StandardResultsSetPagination
from .serializers import (
    BrandSerializer,
    CategorySerializer,
    GameSerializer,
    GameWriteSerializer,
    OrderItemSerializer,
    OrderItemWriteSerializer,
    OrderSerializer,
    OrderWriteSerializer,
    ReviewSerializer,
    ReviewWriteSerializer,
    ShippingAddressSerializer,
)

# Create your views here.


def isAdmin(user):
    return user.groups.filter(name="Admin").exists()


class CategoryViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ["name", "popularity"]
    search_fields = ["name", "description"]
    ordering_fields = ["name"]
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CategorySerializer
        return CategorySerializer

    def get_fallback_queryset(self):
        return Category.objects.all()

    def get_queryset(self):
        try:
            return super().get_queryset()
        except AssertionError:
            return self.get_fallback_queryset()


class BrandViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ["name", "foreign"]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "foreign"]
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        return BrandSerializer

    def get_fallback_queryset(self):
        return Brand.objects.all()

    def get_queryset(self):
        try:
            return super().get_queryset()
        except AssertionError:
            return self.get_fallback_queryset()


class GameViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ["name", "description"]
    filterset_fields = [
        "name",
        "min_age",
        "count_in_stock",
        "rating",
        "price",
        "category__name",
        "brand__name",
    ]
    ordering_fields = ["name", "count_in_stock", "price", "min_age", "rating"]
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [
                IsAuthenticatedOrReadOnly,
            ]
        else:
            permission_classes = [
                DjangoModelPermissions,
            ]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return GameSerializer
        return GameWriteSerializer

    def get_fallback_queryset(self):
        return Game.objects.all()

    def get_queryset(self):
        try:
            return super().get_queryset()
        except AssertionError:
            return self.get_fallback_queryset()


class ReviewViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ["title", "rating", "game__id", "game__name", "user__username"]
    search_fields = ["comment", "title"]
    ordering_fields = ["title", "rating"]
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [
                IsAuthenticatedOrReadOnly,
            ]
        else:
            permission_classes = [
                DjangoModelPermissions,
            ]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ReviewSerializer
        return ReviewWriteSerializer

    def get_queryset_for_admins(self):
        return Review.objects.all()

    def get_fallback_queryset(self):
        if self.action in ["list", "retrieve"]:
            return Review.objects.all()
        else:
            return Review.objects.filter(user_id=self.request.user.id)

    def get_queryset(self):
        if isAdmin(self.request.user):
            return self.get_queryset_for_admins()
        else:
            return self.get_fallback_queryset()


class ShippingAddressViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ["address", "city", "postal_code", "country"]
    search_fields = ["address", "city", "postal_code", "country"]
    ordering_fields = ["address", "city", "postal_code", "country"]
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ShippingAddressSerializer
        return ShippingAddressSerializer

    def get_queryset_for_admins(self):
        return ShippingAddress.objects.all()

    def get_fallback_queryset(self):
        return ShippingAddress.objects.filter(created_by_id=self.request.user.id)

    def get_queryset(self):
        if isAdmin(self.request.user):
            return self.get_queryset_for_admins()
        else:
            return self.get_fallback_queryset()


class OrderViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "user__username",
        "address__city",
        "address__code",
        "address__country",
    ]
    filterset_fields = [
        "user__username",
        "payment_method",
        "address__city",
        "tax_price",
        "total_price",
        "shipping_price",
        "paid",
        "delivered",
    ]
    ordering_fields = ["total_price", "paid", "delivered"]
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return OrderSerializer
        return OrderWriteSerializer

    def get_queryset_for_admins(self):
        return Order.objects.all()

    def get_fallback_queryset(self):
        return Order.objects.filter(user_id=self.request.user.id)

    def get_queryset(self):
        if isAdmin(self.request.user):
            return self.get_queryset_for_admins()
        else:
            return self.get_fallback_queryset()
        
    @action(
        detail=False,
        methods=["post"],
        url_path="create_order",
        # permission_classes=[permissions.IsAuthenticated],
    )
    def create_order(self, request):

        address = ShippingAddress.objects.get(id=request.data['address'])

        order_data = {
            "user": request.user,
            "address": address,
            "total_price": request.data['price']
        }

        order_items = request.data['items']


        new_order = Order.objects.create(**order_data)

        if new_order:
            for item in order_items:
                test = {
                    "game": Game.objects.get(id=item["id"]),
                    "order": new_order,
                    "price": item["price"],
                    "quantity": item["qty"]
                }

                OrderItem.objects.create(**test)

        return Response(
            status=status.HTTP_200_OK,
        )




class OrderItemViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ["game__id", "order__id", "quantity", "price"]
    search_fields = ["game__name", "order__id", "postal_code", "country"]
    ordering_fields = ["quantity", "price"]
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return OrderItemSerializer
        return OrderItemWriteSerializer

    def get_queryset_for_admins(self):
        return OrderItem.objects.all()

    def get_fallback_queryset(self):
        return OrderItem.objects.filter(order_id__in=self.request.user.order_set.all())

    def get_queryset(self):
        if isAdmin(self.request.user):
            return self.get_queryset_for_admins()
        else:
            return self.get_fallback_queryset()
