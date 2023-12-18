from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from api.serializers import ProductSerializer, CategorySerializer, TagSerializer, OrderSerializer, \
    OrderPositionSerializer
from store.models import Product, Category, Tag, Order, OrderPosition


@api_view(['GET', 'POST'])
def product_api(request):
    if request.method == 'GET':
        list_data = Product.objects.filter()
        serializer = ProductSerializer(list_data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_api_detail(request, pk=None):
    one_data = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        serializer =ProductSerializer(one_data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(one_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        one_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects
    serializer_class = ProductSerializer


@api_view(['GET', 'POST'])
def category_api(request):
    if request.method == 'GET':
        list_data = Category.objects.all()
        serializer = CategorySerializer(list_data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def category_api_detail(request, pk=None):
    one_data = get_object_or_404(Category, pk=pk)
    if request.method == 'GET':
        serializer = CategorySerializer(one_data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategorySerializer(one_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        one_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@api_view(['GET', 'POST'])
def tag_api(request):
    if request.method == 'GET':
        list_data = Tag.objects.all()
        serializer = TagSerializer(list_data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def tag_api_detail(request, pk=None):
    one_data = get_object_or_404(Tag, pk=pk)
    if request.method == 'GET':
        serializer = TagSerializer(one_data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TagSerializer(one_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        one_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


@api_view(['GET', 'POST'])
def order_api(request):
    if request.method == 'GET':
        list_data = Order.objects.filter()
        serializer = OrderSerializer(list_data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def order_api_detail(request, pk=None):
    one_data = get_object_or_404(Order, pk=pk)
    if request.method == 'GET':
        list_data = Order.objects.filter()
        serializer = OrderSerializer(one_data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrderSerializer(one_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        one_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.filter()
    serializer_class = OrderSerializer


@api_view(['GET', 'POST'])
def order_pos_api(request):
    if request.method == 'GET':
        list_data = OrderPosition.objects.filter()
        serializer = OrderPositionSerializer(list_data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = OrderPositionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def order_pos_api_detail(request, pk=None):
    one_data = get_object_or_404(OrderPosition, pk=pk)
    if request.method == 'GET':
        list_data = OrderPosition.objects.filter()
        serializer = OrderPositionSerializer(one_data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrderPositionSerializer(one_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        one_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderPosition.objects.filter()
    serializer_class = OrderPositionSerializer