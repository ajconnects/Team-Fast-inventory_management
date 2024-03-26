from django.urls import path
from  . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("add", views.add_product, name='add_product'),
    path("update", views.update_product, name='update_product'),
    path("delete", views.delete_product, name='delete_product'),
]