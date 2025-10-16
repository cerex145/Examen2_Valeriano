from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    # Mostrar cantidad de productos en la categoría (opcional)
    products_count = serializers.IntegerField(source='products.count', read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'products_count']

class ProductSerializer(serializers.ModelSerializer):
    # campo opcional extra: nombre de la categoría embebido para mejor UX (punto extra)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'quantity', 'price', 'category', 'category_name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'category_name']
