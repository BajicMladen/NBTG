from apps.user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    popularity = models.IntegerField(
        default=0,
        validators=PERCENTAGE_VALIDATOR,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | {self.popularity}"


class Brand(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    foreign = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True, default="/placeholder.png")
    link = models.URLField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default="/placeholder.png")
    min_age = models.IntegerField(null=True, blank=True, default=0)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    count_in_stock = models.IntegerField(null=True, blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        validators=PERCENTAGE_VALIDATOR,
    )
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.game.name} | {self.user.get_full_name()} | {self.rating}"


class ShippingAddress(models.Model):
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.id} | {self.address} | {self.city} | {self.country}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField(max_length=200, null=True, blank=True)
    address = models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, null=True)
    tax_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    total_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    shipping_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} | {self.user.get_full_name()} | {self.total_price}"


class OrderItem(models.Model):
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.id} | {self.game.name} | {self.quantity}"
