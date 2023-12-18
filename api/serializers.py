from rest_framework import serializers
from store.models import Product, Category, Tag, Order, OrderPosition


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPosition
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    store = OrderPositionSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

