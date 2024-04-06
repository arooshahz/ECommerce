from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Category


class HomeView(View):
    def get(self, request):
        products = Product.objects.filter(available=True)
        best_seller = products.order_by('-Sales_number')[:4]
        suggested = products[:4]
        return render(request, 'home/home.html',
                      {'products': products, 'best_seller': best_seller, 'suggested': suggested})


class ProductsView(View):
    def get(self, request):
        products = Product.objects.filter(available=True)
        return render(request, 'home/home.html', {'products': products})


class CategoryView(View):
    def get(self, request, slug):
        products = Product.objects.filter(available=True)
        category = get_object_or_404(Category, slug=slug)
        category_product = products.filter(category=category)
        return render(request, 'home/test.html', {'products': category_product})


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'home/detail.html', {'product': product})
