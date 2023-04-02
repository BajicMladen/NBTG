from apps.shop.views import (
    BrandViewSet,
    CategoryViewSet,
    GameViewSet,
    OrderItemViewSet,
    OrderViewSet,
    ReviewViewSet,
    ShippingAddressViewSet,
)
from apps.user.views import UserViewset
from rest_framework import routers

api = routers.DefaultRouter()
api.trailing_slash = "/?"

api.register(r"user", UserViewset, "user")
api.register(r"category", CategoryViewSet, "category")
api.register(r"brand", BrandViewSet, "brand")
api.register(r"game", GameViewSet, "game")
api.register(r"review", ReviewViewSet, "review")
api.register(r"shipping-address", ShippingAddressViewSet, "shipping-address")
api.register(r"order", OrderViewSet, "order")
api.register(r"order-item", OrderItemViewSet, "order-item")
