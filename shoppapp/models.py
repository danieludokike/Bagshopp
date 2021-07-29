from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """STORES PRODUCT DETAILS"""
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=100)
    discount_price = models.DecimalField(default=0.0, decimal_places=2, max_digits=100)
    product_image = models.ImageField(upload_to="Products/")
    description = models.TextField(max_length=500)
    featured_tag = models.BooleanField(default=True,
                                       help_text="Check this field if you want this product to be in the featured list"
                                       )
    date_added = models.DateTimeField(auto_now_add=True)
    added_to_cart = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.name} ${self.price}"


class ProductOrder(models.Model):
    """STORES THE ORDERS ON RECORD"""
    user = models.ForeignKey(User, related_name="ordered_by", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product_order", on_delete=models.CASCADE)
    address = models.CharField(max_length=100, help_text="Address of delivery")
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    order_date = models.DateTimeField(auto_now_add=True, help_text="Date the product is ordered")
    paid = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False, help_text="Marked when the product is delivered")
    pending = models.BooleanField(default=True, help_text="It's unmarked when the product is delvered")

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.product} {self.product.price}"


class UserContact(models.Model):
    """STORES THE CONTACT DETAILS OF USER"""
    name = models.CharField(max_length=100),
    email = models.EmailField(max_length=125)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=500)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    """STORES THE DETAILS OF SUBSCRIBERS"""
    user_email = models.EmailField(max_length=125)

    def __str__(self):
        return self.user_email
