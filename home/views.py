from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Category
from django.core.paginator import Paginator


class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        best_seller = products.order_by('-Sales_number')[:4]
        suggested = products[:4]

        return render(request, 'home/home.html',
                      {'products': products, 'best_seller': best_seller, 'suggested': suggested,
                       'categories': categories})


class ProductsView(View):
    def get(self, request, page_number=1):
        products_list = Product.objects.filter(available=True)
        products = Paginator(products_list, 9)
        prev_num = int(page_number) - 1
        next_num = int(page_number) + 1
        last_page = products.page(1).paginator.num_pages

        return render(request, 'home/products.html',
                      {'products': products.page(page_number), 'page_number': page_number,
                       'prev_num': prev_num,
                       'next_num': next_num,
                       'last_page': last_page,
                       'current_page': products.page(page_number).number})


class CategoryView(View):
    def get(self, request, slug, page_number=1):
        products = Product.objects.filter(available=True)
        category = get_object_or_404(Category, slug=slug)
        category_product = products.filter(category=category)
        products_list = Paginator(category_product, 9)
        prev_num = int(page_number) - 1
        next_num = int(page_number) + 1
        last_page = products_list.page(1).paginator.num_pages
        return render(request, 'home/category.html',
                      {'products': products_list, 'category': category, 'page_number': page_number,
                       'prev_num': prev_num,
                       'next_num': next_num,
                       'last_page': last_page, 'current_page': products_list.page(page_number).number})


class ProductBasedOnPrice(View):
    def get(self, request, min_price, max_price):
        products = Product.objects.filter(price__gt=min_price, price__lt=max_price)
        return render(request, 'home/test.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        print(product.features.name)
        return render(request, 'home/detail.html', {'product': product})
