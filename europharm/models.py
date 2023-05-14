from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=0)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    instructions = models.FileField(default=None, upload_to='instructions/')
    last_viewed = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Profile(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'profiles'

    def __str__(self):
        return self.username


class Order(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    index = models.DecimalField(max_digits=5, decimal_places=0)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    price = models.ForeignKey(Product.price, related_name='product', on_delete=models.CASCADE)
    buyer = models.ForeignKey(Product.price, related_name='product', on_delete=models.CASCADE)