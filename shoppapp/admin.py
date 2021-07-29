from django.contrib import admin

from .models import (
    Product, ProductOrder,
    UserContact, Subscriber,
)

# OWN MODELS
admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(UserContact)
admin.site.register(Subscriber)
