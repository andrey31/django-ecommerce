from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category (models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    category = models.CharField(max_length = 100)

    def __str__(self):
        return self.category

class Product (models.Model):
    #class Meta:
    #verbose_name = 'Producto'
    #verbose_name_plural = 'Productos'
    product = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    description = models.CharField(max_length = 50)
    stock = models.PositiveIntegerField(default = 0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'gallery', default = 'gallery/static/images/no-img.jpg')

    def __str__(self):
        return self.product

class Order (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date = models.DateTimeField(auto_now_add=True)
    