from django.shortcuts import render
#import django_filters.rest_framework
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

class ProductFilter (filters.FilterSet):
    min_stock = filters.NumberFilter(field_name='stock', lookup_expr='gte')
    category = filters.CharFilter(field_name='category')
    
    class Meta:
        model: Product
        fields = ['category', 'min_stock']

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.DjangoFilterBackend,]
    #filterset_fields =['category',]
    filterset_class = ProductFilter
    
    