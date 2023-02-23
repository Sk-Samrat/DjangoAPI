from rest_framework import serializers
from CloudKitchen.models import Products, ProductCategory, ProductOffer, OrderItem, Order


class ProductSerializer(serializers.ModelSerializer):
    main_image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Products
        fields = ('product_id', 'product_category', 'product_name',
                  'product_description', 'product_price', 'main_image', 'product_uom', 'product_quantity')


class ProductCategorySerializer(serializers.ModelSerializer):
    main_image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = ProductCategory
        fields = ('product_id', 'product_category', 'product_name',
                  'product_price', 'main_image')


class ProductOfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductOffer
        # fields = ('id', 'title', 'url', 'description', 'price')
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        # fields = ('id', 'title', 'url', 'description', 'price')
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        # fields = ('id', 'title', 'url', 'description', 'price')
        fields = '__all__'
