from django.contrib import admin
from .models import Products,ProductCategory,ProductOffer,OrderItem,Order,Orderall

# Register your models here.

# class ProductAdmin(admin.ModelAdmin):
#     list_display=['ProductId','ProductCategory','ProductName','ProductDesc','ProductPrice','ProductImage']

admin.site.register(Products)
admin.site.register(ProductCategory)
admin.site.register(ProductOffer)
admin.site.register(OrderItem)
admin.site.register(Order)

@admin.register(Orderall)
class OrderallAdmin(admin.ModelAdmin):
    list_display = ("order_id", "product_id_id","product_name","order_quantity","unit_price","product_uom","total_price","customer_name","seller_name","order_date")
