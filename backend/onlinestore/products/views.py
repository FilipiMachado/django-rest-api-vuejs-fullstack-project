from django.http import JsonResponse

from .models import Product, Manufacturer


def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values())}
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try:
        product = Product.object.get(pk=pk)
        data = {"product": {
            "name": product.name,
            "manufacturer": product.manufacturer.name,
            "description": product.description,
            "photo": product.photo.url,
            "price": product.price,
            "shipping_price": product.shipping_price,
            "quantity": product.quantity,
        }}
        response = JsonResponse(data)
    
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "Product not found!",
            }},
            status=404)
    
    return response

""" from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    
class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html" """