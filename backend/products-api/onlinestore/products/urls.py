from django.urls import path

from .views import product_list, product_detail, manufacturer_list, manufacturer_info  # ProductDetailView, ProductListView

urlpatterns = [
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>/", product_detail, name="product-detail"),
    path("manufacturers/", manufacturer_list, name="manufacturer-list"),
    path("manufacturers/<int:pk>/", manufacturer_info, name="manufacturer-info"),
]
