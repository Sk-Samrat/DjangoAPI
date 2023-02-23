from django.db import models
from datetime import date
from view_table.models import ViewTable
# Create your models here.


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_category = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=250)
    product_price = models.IntegerField()
    main_image = models.ImageField(upload_to="Photos", default="")
    product_uom = models.CharField(max_length=10, default="Dish")
    product_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


class ProductCategory(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_category = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField(default=0)
    main_image = models.ImageField(upload_to="Photos", default="")

    def __str__(self):
        return self.product_name


class ProductOffer(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=50, default="Sk Samrat")
    seller_name = models.CharField(max_length=50, default="Jayanta Dutta")
    total_price = models.IntegerField()
    order_date = models.DateField(default=date.today)

    def __str__(self):
        return self.order_id

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, to_field='order_id',on_delete=models.CASCADE)
    # order_id = models.CharField(max_length=50)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    order_quantity = models.IntegerField()
    unit_price = models.IntegerField()
    product_uom = models.CharField(max_length=10, default="Dish")
    total_price = models.IntegerField()

    def __str__(self):
        return self.product_name
        
# View table
# class Orderitem_View(ViewTable):
    # order_id = models.CharField(max_length=50)
    # product_id = models.IntegerField()
    # product_name = models.CharField(max_length=50)
    # order_quantity = models.IntegerField()
    # unit_price = models.IntegerField()
    # product_uom = models.CharField(max_length=10, default="Dish")
    # total_price = models.IntegerField()
    # customer_name = models.CharField(max_length=50, default="Sk Samrat")
    # seller_name = models.CharField(max_length=50, default="Jayanta Dutta")
    # order_date = models.DateField(default=date.today)

    # You must implement get_query method.
    # @classmethod
    # def get_query(self):
        # return Book.objects.values('category').annotate(count=models.Count('category')).query
        # return Order.objects.values('order_id','').query
        # You can also write:
        # return 'SELECT "polls_Order"."order_id", "polls_OrderItem"."product_id", "polls_OrderItem"."product_name", "polls_OrderItem"."order_quantity", "polls_OrderItem"."unit_price", "polls_OrderItem"."product_uom", "polls_OrderItem"."total_price", "polls_Order"."customer_name", "polls_Order"."seller_name", "polls_Order"."order_date" FROM "polls_Order","polls_OrderItem" WHERE "polls_Order"."order_id"="polls_OrderItem.order_id"' 
        # return 'SELECT "Order"."order_id", "OrderItem"."product_id", "OrderItem"."product_name", "OrderItem"."order_quantity", "OrderItem"."unit_price", "OrderItem"."product_uom", "OrderItem"."total_price", "Order"."customer_name", "Order"."seller_name", "Order"."order_date" FROM "Order","OrderItem" WHERE "Order"."order_id"="OrderItem.order_id"'
        

class Orderall(models.Model):
    id = models.IntegerField(primary_key=True)
    order_id = models.CharField(max_length=50)
    product_id_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    order_quantity = models.IntegerField()
    unit_price = models.IntegerField()
    product_uom = models.CharField(max_length=10, default="Dish")
    total_price = models.IntegerField()
    customer_name = models.CharField(max_length=50, default="Sk Samrat")
    seller_name = models.CharField(max_length=50, default="Jayanta Dutta")
    order_date = models.DateField(default=date.today)

    class Meta:
        managed = False
        db_table = "order_all_view"