from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view

from CloudKitchen.models import Products,ProductCategory,ProductOffer,OrderItem,Order
from CloudKitchen.serializers import ProductSerializer,ProductCategorySerializer,ProductOfferSerializer,CartItemSerializer,OrderSerializer

from django.core.files.storage import default_storage

# Create your views here.


@csrf_exempt
def productApi(request, id=0):
    if request.method == 'GET':
        departments = Products.objects.all()
        departments_serializer = ProductSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'POST':
        print(request.POST)
        # product_data=FormParser().parse(request)
        product_data = MultiPartParser().parse(request.POST)
        # product_data=JSONParser().parse(request)
        product_serializer=ProductSerializer(data=product_data,many=True)
        # product_serializer = ProductSerializer(data=request.POST)
        print(product_serializer)
        if product_serializer.is_valid():
            product_serializer.save()
            print(product_serializer.data)
            return JsonResponse("Added Successfully", safe=False)
        # return JsonResponse("Failed to Add", safe=False)
        return JsonResponse(product_serializer.errors, safe=False)

class CreatePost(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def productCategoryApi(request):
    if request.method == 'GET':
        products = ProductCategory.objects.all()
        products_serializer = ProductCategorySerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)

@api_view(['GET'])
def productOfferApi(request):
    if request.method == 'GET':
        products = ProductOffer.objects.all()
        products_serializer = ProductOfferSerializer(products, many=True)
        return Response(products_serializer.data)
        
@api_view(['GET','POST'])
def orderItemApi(request, id=0):
    if request.method == 'GET':
        cartitem = OrderItem.objects.all()
        cartitem_serializer = CartItemSerializer(cartitem, many=True)
        return Response(cartitem_serializer.data)
    elif request.method == 'POST':
        #parser_classes = [MultiPartParser, FormParser, JSONParser]
        cartitem=JSONParser().parse(request)
        # print('Order Id: ',request.POST.order_id)
        print(cartitem)
        cartitem_serializer=CartItemSerializer(data=cartitem,many=True)
        print(cartitem_serializer)
        #return Response("Added Successfully")
        # product_data=FormParser().parse(request)
        # product_data = MultiPartParser().parse(request.POST)
        #cartitem=JSONParser().parse(request)
        #print(cartitem)
        #cartitem_serializer=CartItemSerializer(data=cartitem,many=True)
        #cartitem_serializer=CartItemSerializer(data=request.POST,many=True)
        #product_serializer = ProductSerializer(data=request.POST)
        #print(cartitem_serializer)
        if cartitem_serializer.is_valid():
            cartitem_serializer.save()
            print(cartitem_serializer.data)
            return Response("Added Successfully")
        # return JsonResponse("Failed to Add", safe=False)
        return Response(cartitem_serializer.errors)

@api_view(['GET','POST'])
def orderApi(request, id=0):
    if request.method == 'GET':
        order = Order.objects.all()
        order_serializer = OrderSerializer(order, many=True)
        return Response(order_serializer.data)
    elif request.method == 'POST':
        #parser_classes = [MultiPartParser, FormParser, JSONParser]
        order=JSONParser().parse(request)
        # print('Order Id: ',request.POST.order_id)
        print(order)
        order_serializer=OrderSerializer(data=order,many=True)
        print(order_serializer)
        #return Response("Added Successfully")
        # product_data=FormParser().parse(request)
        # product_data = MultiPartParser().parse(request.POST)
        #cartitem=JSONParser().parse(request)
        #print(cartitem)
        #cartitem_serializer=CartItemSerializer(data=cartitem,many=True)
        #cartitem_serializer=CartItemSerializer(data=request.POST,many=True)
        #product_serializer = ProductSerializer(data=request.POST)
        #print(cartitem_serializer)
        if order_serializer.is_valid():
            order_serializer.save()
            print(order_serializer.data)
            return Response("Added Successfully")
        # return JsonResponse("Failed to Add", safe=False)
        return Response(order_serializer.errors)
        
@api_view(['GET'])
def orderIdApi(request):
    if request.method == 'GET':
        #orderid = Order.objects.get(id=id).order_by("-id")[0]
        #res = Order.objects.filter().aggregate(max_id=Max('pk'))
        #print(res.get('max_id'))
        orderid = Order.objects.last().id
        print(orderid)
        #order_serializer = OrderSerializer(orderid, many=True)
        #return Response(order_serializer.data)
        return Response(orderid)
        
