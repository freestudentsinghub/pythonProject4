from django.core.cache import cache
from config.settings import CACHE_ENABLED


from .models import Product

def get_product_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products

def get_products_by_category(category):
    products = Product.objects.filter(category=category).order_by('-created_at')
    return products

