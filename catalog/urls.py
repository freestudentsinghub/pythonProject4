from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, ProductDetailView, ProductList, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductsByCategoryView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_ditail'),
    path('home', ProductList.as_view(), name='product_list'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:pk>/', ProductsByCategoryView.as_view(), name='products_by_category'),
]


