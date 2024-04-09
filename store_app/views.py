from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .models import Product, Supplier
from .forms import ProductForm, SupplierForm

# Create your views here.

# The Home Page for All Views
class HomePageView(TemplateView):
    template_name = 'store_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


#The User Login Page 
def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #User: User is a model provided by Django's authentication system. It represents a user account in the database and comes with fields like username, password, email, first name, last name, etc. and use create_user to create and add to the database.
        user_detail = User.objects.create_user(username, email, pass1)
        user_detail.first_name= fname
        user_detail.last_name = lname

        user_detail.save()

        messages.success(request, "Your Account has been successfully created")

        return redirect('signin')

    return render(request, 'store_app/signup.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        #it to check the authenticate of the user information
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'store_app/signin.html', {
                'fname': fname
            })
        
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')
        

    return render(request, 'store_app/signin.html')

def user_page(request):
    if request.method == 'POST':
        user = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=user, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('user-page')
        
    return render(request, 'store_app/user_page.html')

def signout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('home')

# The Create View to create New form for Product and Supplier
class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'store_app/add_product.html'
    success_url = 'list-product'

class AddSupplierView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'store_app/add_supplier.html'
    success_url = 'list-supplier'

#The List View to View all Product and Supplier
class ListOfProduct(ListView):
    model = Product
    template_name = 'store_app/list_product.html'
    context_object_name = 'products'

class ListOfSupplier(ListView):
    model = Supplier
    template_name = 'store_app/list_supplier.html'
    context_object_name = 'suppliers'

#The Details View for Product and Supplier to get each details
class SupplierDetail(DetailView):
    template_name = 'store_app/detail_supplier.html'
    model = Supplier
    context_object_name = 'supplier'

class ProductDetail(DetailView):
    model = Product
    template_name = 'store_app/detail_product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'name'
    slug_field = 'name'

# The Update View for Product and Supplier
class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'store_app/add_product.html'
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_object(self):
        return get_object_or_404(Product, name=self.kwargs['name'])
    
    def get_success_url(self) -> str:
        return reverse_lazy('product-detail', kwargs={'name':self.object.name})
    
class SupplierUpdate(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'store_app/add_supplier.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    
    def get_object(self):
        return get_object_or_404(Supplier, username=self.kwargs['username'])
    
    def get_success_url(self) -> str:
        return reverse_lazy('supplier-detail', kwargs={'pk':self.object.pk})  #{'username':self.object.username}

#The Delete View for Product and Supplier
class DeleteProduct(DeleteView):
    model = Product
    template_name = 'store_app/delete_product.html'
    success_url = reverse_lazy('list-product')
    slug_field = 'name'
    slug_url_kwarg = 'name'

class DeleteSupplier(DeleteView):
    model = Supplier
    template_name = 'store_app/delete_supplier.html'
    success_url = reverse_lazy('list-supplier')
    slug_field = 'username'
    slug_url_kwarg = 'username'