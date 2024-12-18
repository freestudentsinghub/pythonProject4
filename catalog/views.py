
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product

class HomeView(TemplateView):
    template_name = "catalog/home.html"

# def home(request):
#     return render(request, 'home.html')

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

# def contacts(request):
#     return render(request, 'contacts.html')


class ProductDetailView(DetailView):
    model = Product

# def product_ditail(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {
#         "product_name": product.name,
#         "product_description": product.description,
#         "product_image": product.image,
#         "product_category": product.category,
#         "product_cost": product.cost,
#         "product_created_at": product.created_at,
#         "product_updated_at": product.updated_at,
#                }
#     return render(request, 'product_detail.html', context)

# catalog/product_list.html detail


class ProductList(ListView):
    model = Product


# def product_list(request):
#     products = Product.objects.all()
#     context = {
#         "products": products,
#     }
#     return render(request, 'home.html', context=context)
