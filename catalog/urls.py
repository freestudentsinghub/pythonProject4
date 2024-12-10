from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_ditail

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('', contacts, name='contacts'),
    path('product/<int:pk>', product_ditail, name='product_ditail')
]


