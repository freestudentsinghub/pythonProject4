from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView, View

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


    def get_initial(self):
        initial = super().get_initial()
        initial["owner"] = self.request.user
        return initial

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("product.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied

    def test_func(self):
        return self.request.user == self.get_object().owner

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied
        return redirect('catalog:product_list')

class HomeView(TemplateView):
    template_name = "catalog/home.html"


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(DetailView):
    model = Product


class ProductList(ListView):
    model = Product


class ProductModeratorsView(LoginRequiredMixin, UserPassesTestMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm('catalog.delete_product'):
            return HttpResponseForbidden("У вас нет прав доступа на удаление")

        product.delete()

        return redirect('catalog:product_list')

    def test_func(self):
        return self.request.user == self.get_object().owner

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied
        return redirect('catalog:product_list')

