from rest_framework import serializers
from .models import Product

#serializers.HyperlinkedModelSerializer
class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, use_url=True
    )
    class Meta:
        model = Product
        fields = '__all__'