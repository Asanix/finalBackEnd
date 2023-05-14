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


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=255, null=False)
    lname = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    phone = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=255, null=False)
    zip = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    state = models.CharField(max_length=255, null=False)
    address = models.TextField(null=False)
    totalPrice = models.FloatField(null=False)
    payment = models.CharField(max_length=255, null=False)
    payment_id = models.CharField(max_length=255, null=True)
    orderStatus = (
        ('Pending', 'Pending'),
        ('Out for shipping', 'Out for shipping'),
        ('Delivered', 'Delivered'),
    )
    status = models.CharField(max_length=255, choices= orderStatus, default='Pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True )

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)

    def __str__(self):
        return '{} {}'.format(self.order.id, self.order.tracking_no)
