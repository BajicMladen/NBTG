from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Brand, Category, Game, Order, OrderItem, Review, ShippingAddress
from .serializers import (
    BrandSerializer,
    CategorySerializer,
    GameSerializer,
    GameWriteSerializer,
    OrderItemSerializer,
    OrderSerializer,
    ReviewSerializer,
    ShippingAddressSerializer,
)

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ["name", "popularity"]
    search_fields = ["name", "description"]
    ordering_fields = ["name"]

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
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
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
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ["title", "rating", "game__name", "user__username"]
    search_fields = ["comment", "title"]
    ordering_fields = ["title", "rating"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ReviewSerializer
        return ReviewSerializer

    def get_fallback_queryset(self):
        return Review.objects.all()

    def get_queryset(self):
        try:
            return super().get_queryset()
        except AssertionError:
            return self.get_fallback_queryset()


class ShippingAddressViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ["address", "city", "postal_code", "country"]
    search_fields = ["address", "city", "postal_code", "country"]
    ordering_fields = ["address", "city", "postal_code", "country"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ShippingAddressSerializer
        return ShippingAddressSerializer

    def get_fallback_queryset(self):
        return ShippingAddress.objects.all()

    def get_queryset(self):
        try:
            return super().get_queryset()
        except AssertionError:
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

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return OrderSerializer
        return OrderSerializer

    def get_fallback_queryset(self):
        return Order.objects.all()

    def get_queryset(self):
        try:
            return super().get_queryset()
        except AssertionError:
            return self.get_fallback_queryset()


class OrderItemViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ["game__id", "order__id", "quantity", "price"]
    search_fields = ["game__name", "order__id", "postal_code", "country"]
    ordering_fields = ["quantity", "price"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return OrderItemSerializer
        return OrderItemSerializer

    def get_fallback_queryset(self):
        return OrderItem.objects.all()

    def get_queryset(self):
        try:
            return super().get_queryset()
        except AssertionError:
            return self.get_fallback_queryset()
