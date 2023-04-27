from django.urls import path

from .views import product_list  # ProductDetailView, ProductListView

urlpatterns = [
    path("products/", product_list, name="product-list"),
]
