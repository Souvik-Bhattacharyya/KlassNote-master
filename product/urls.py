from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products_view, name='products'),
    path('filter/<int:category>/', views.all_products_view, name='filter_products'),
    path('details/<int:pid>/', views.product_details_view, name="product_details")
]
