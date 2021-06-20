from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from . import models


def all_products_view(request, category=None):
    categories = models.ProductCategory.objects.all()
    if category:
        all_products = Paginator(
            models.Product.objects.filter(category__id=category), 24)
    else:
        all_products = Paginator(models.Product.objects.all(), 24)
    all_products = all_products.get_page(request.GET.get('page'))
    return render(request, 'product.html',
                  {'all_products': all_products, 'categories': categories})


def product_details_view(request, pid):
    try:
        details = models.Product.objects.get(id=pid)
    except models.Product.DoesNotExist:
        return redirect(reverse('index'))
    images = details.get_images[1:]
    return render(request, 'product_details.html',
                  {'details': details, 'images': images, 'index': range(1, len(images)+1)})
