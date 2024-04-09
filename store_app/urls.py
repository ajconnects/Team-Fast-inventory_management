from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path("signup", views.signup, name='signup'),
    path("signout", views.signout, name='signout'),
    path("signin", views.signin, name='signin'),
    path("user-page", views.user_page, name='user-page'),
    path("add-product", views.AddProductView.as_view(), name="add-product"),
    path("add-supplier", views.AddSupplierView.as_view(), name="add-supplier"),
    #path("thank-you", views.ThankYouView.as_view(), name="thank-you"), 
    path("list-product", views.ListOfProduct.as_view(), name="list-product"),
    path("list-supplier", views.ListOfSupplier.as_view(), name="list-supplier"),
    path("list-supplier/<int:pk>", views.SupplierDetail.as_view(), name="supplier-detail"),
    path("list-product/<str:name>", views.ProductDetail.as_view(), name="product-detail"),
    path("product/<str:name>/update/", views.ProductUpdate.as_view(), name="update-product"),
    path("supplier/<str:username>/update/", views.SupplierUpdate.as_view(), name='update-supplier'),
    path("product/<str:name>/delete/", views.DeleteProduct.as_view(), name="delete-product"),
    path("supplier/<str:username>/delete/", views.DeleteSupplier.as_view(), name='delete-supplier')
    ]
   
