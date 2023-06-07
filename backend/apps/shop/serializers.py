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

from datetime import datetime


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    brand_name = serializers.SerializerMethodField()
    num_of_reviews = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = [
            "id",
            "user",
            "category",
            "stripe_code",
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
            "category_name",
            "brand_name"
        ]

    def get_category_name(self, instance):
        return instance.category.name if instance.category else None

    def get_brand_name(self, instance):
        return instance.brand.name if instance.brand else None

    def get_num_of_reviews(self, instance):
        return instance.review_set.all().count()
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%m/%d/%y")


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
            "stripe_code"
        ]


class ReviewSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    user_image = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = [
            'game',
            'user_name',
            'user_image',
            'title',
            'rating',
            'comment',
            'created_at'
        ]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")
    
    def get_user_name(self, instance):
        return instance.user.first_name +' '+ instance.user.last_name
    
    def get_user_image(self, instance):
        return instance.user.image.url if instance.user.image else None

class ReviewWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = "__all__"


class OrderWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    order_items = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    paid = serializers.SerializerMethodField()
    delivered = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = [
            "id",
            "payment_method",
            "tax_price",
            "total_price",
            "shipping_price",
            "paid",
            "paid_at",
            "delivered",
            "delivered_at",
            "created_at",
            "user",
            "address",
            "order_items",
            "user_name"
        ]

    def get_paid(self, instance):
        return  'Yes' if instance.paid else 'No'
    
    def get_delivered(self, instance):
        return  'Yes' if instance.paid else 'No'

    def get_address(self, instance):
        return instance.address.address or None
    
    def get_user_name(self, instance):
        return instance.user.username or None
    
    def get_order_items(self, instance):
        order_items = OrderItem.objects.filter(order_id=instance.id)
        return OrderItemSerializer(order_items, many=True).data
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")



class OrderItemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    game = serializers.SerializerMethodField()
    class Meta:
        model = OrderItem
        fields = [
            'game',
            'order',
            'quantity',
            'price'
        ]

    def get_game(self, instance):
        return GameSerializer(instance.game).data
