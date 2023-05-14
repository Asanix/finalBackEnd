from django.urls import path, include
from django.contrib import admin
from . import views
from .views import *

urlpatterns = [
    path('', index.as_view(), name='main'),
    path('basket/', basket.as_view(), name='basket'),
    path('up/', up.as_view(), name='up'),
    path('down/', down.as_view(), name='down'),
    path('alphabet/', alphabet.as_view(), name='alphabet'),
    path('admin/', admin.site.urls),
    path('', include('login.urls', namespace='login')),
    path('acc/', acc.as_view(), name='acc'),
    path('log/', log.as_view(), name='log'),
    path('reg/', register.as_view(), name='reg'),
    path('product_detail/<slug:slug>', detail.as_view(), name='detail'),
    path('add_product/', add_product_admin.as_view(), name='add_product_admin'),
    path('add_product_user/', add_product_user.as_view(), name='add_product_user'),
    path('add_user/', add_user.as_view(), name='add_user'),
    path('admin_page/', admin_page.as_view(), name='admin_page'),
    path('delete_product/', delete_product.as_view(), name='delete_product'),
    path('delete_user/', delete_user.as_view(), name='delete_user'),
    path('edit_product/<int:id>/', edit_product.as_view(), name='edit_product'),
    path('edit_user/<int:id>/', edit_user.as_view(), name='edit_user'),
    path('search/', Search.as_view(), name='search'),
    //asd
]

