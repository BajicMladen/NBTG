from apps.shop.models import (
    Brand,
    Category,
    Game,
    Order,
    OrderItem,
    Review,
    ShippingAddress,
)
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    num_of_reviews = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = [
            "id",
            "user",
            "category",
            "brand",
            "name",
            "image",
            "min_age",
            "description",
            "rating",
            "count_in_stock",
            "price",
            "created_at",
            "num_of_reviews",
        ]

    def get_category(self, instance):
        return instance.category.name if instance.category else None

    def get_brand(self, instance):
        return instance.brand.name if instance.brand else None

    def get_num_of_reviews(self, instance):
        return instance.review_set.all().count()


class GameWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            "user",
            "category",
            "brand",
            "name",
            "image",
            "min_age",
            "description",
            "rating",
            "count_in_stock",
            "price",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
