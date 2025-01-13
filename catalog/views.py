
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Product

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

class HomeView(TemplateView):
    template_name = "catalog/home.html"


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(DetailView):
    model = Product


class ProductList(ListView):
    model = Product

