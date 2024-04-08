from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/create/', views.create_product, name='create_product'),
    path('supplier/create/', views.create_supplier, name='create_supplier'),
    path('product/list/', views.product_list, name='product_list'),
    path('supplier/list/', views.supplier_list, name='supplier_list'),
    path('product/update/<int:product_id>/', views.update_product, name='update_product'),
    path('supplier/update/<int:supplier_id>/', views.update_supplier, name='update_supplier'),
    path('product/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('supplier/delete/<int:supplier_id>/', views.delete_supplier, name='delete_supplier'),
]