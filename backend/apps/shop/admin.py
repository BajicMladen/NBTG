from apps.shop.models import (
    Brand,
    Category,
    Game,
    Order,
    OrderItem,
    Review,
    ShippingAddress,
)
from django.contrib import admin

# Register your models here.

admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)
