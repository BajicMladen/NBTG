from django.shortcuts import render
from rest_framework import decorators, mixins, status, viewsets

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


class CategoryViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
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


class BrandViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    def get_serializer_class(self):
        return BrandSerializer

    def get_fallback_queryset(self):
        return Brand.objects.all()

    def get_queryset(self):
        try:
            return super().get_queryset()
        except AssertionError:
            return self.get_fallback_queryset()


class GameViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
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


class ReviewViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
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


class ShippingAddressViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
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


class OrderViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
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


class OrderItemViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
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
