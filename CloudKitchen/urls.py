# from django.conf.urls import re_path
from django.urls import re_path,path
from CloudKitchen import views
from .views import CreatePost

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^product$', views.productApi),
    re_path(r'^product/([0-9]+)$', views.productApi),
    # re_path(r'^createproduct$', CreatePost.as_view(), name='createpost'),
    re_path(r'^productcategory$', views.productCategoryApi),
    re_path(r'^productoffer$', views.productOfferApi),
    re_path(r'^orderitem$', views.orderItemApi),
    re_path(r'^order$', views.orderApi),
    re_path(r'^orderid$', views.orderIdApi),
    # re_path(r'^orderitem$', CreatePost.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
