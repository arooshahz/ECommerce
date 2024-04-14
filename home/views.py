from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from .models import Product, Category
from django.core.paginator import Paginator


class HomeView(View):

    def get(self, request):
        categories = Category.objects.filter(is_sub=False)
        products = Product.objects.filter(available=True)
        if request.GET.get('search'):
            search_query = request.GET.get('search')
            products = products.filter(
                Q(description__icontains=search_query) |
                Q(name__icontains=search_query)
            )
        best_seller = products.order_by('-Sales_number')[:4]
        suggested = products[:4]
        return render(request, 'home/home.html',
                      {'products': products, 'best_seller': best_seller, 'suggested': suggested,
                       'categories': categories})


class ProductsView(View):
    def get(self, request, page_number=1):
        categories = Category.objects.filter(is_sub=False)
        products_list = Product.objects.filter(available=True)
        products = Paginator(products_list, 9)
        prev_num = int(page_number) - 1
        next_num = int(page_number) + 1
        last_page = products.page(1).paginator.num_pages

        return render(request, 'home/products.html',
                      {'products': products.page(page_number), 'categories': categories, 'page_number': page_number,
                       'prev_num': prev_num,
                       'next_num': next_num,
                       'last_page': last_page,
                       'current_page': products.page(page_number).number})

    def post(self, request, page_number):
        min_price = request.POST.get('min-price')
        max_price = request.POST.get('max-price')

        return redirect(
            reverse('home:product_price', kwargs={'min_price': min_price, 'max_price': max_price, 'page_number': 1}))


class CategoryView(View):
    def get(self, request, slug, page_number=1):
        categories = Category.objects.filter(is_sub=False)
        products = Product.objects.filter(available=True)
        category = get_object_or_404(Category, slug=slug)
        category_product = products.filter(category=category)
        products_list = Paginator(category_product, 9)
        prev_num = int(page_number) - 1
        next_num = int(page_number) + 1
        last_page = products_list.page(1).paginator.num_pages
        return render(request, 'home/category.html',
                      {'products': products_list, 'categories': categories, 'category': category,
                       'page_number': page_number,
                       'prev_num': prev_num,
                       'next_num': next_num,
                       'last_page': last_page, 'current_page': products_list.page(page_number).number})


class ProductBasedOnPrice(View):
    def get(self, request, min_price, max_price, page_number=1):
        categories = Category.objects.filter(is_sub=False)
        products_list = Product.objects.filter(price__gt=min_price, price__lt=max_price)
        products = Paginator(products_list, 9)
        prev_num = int(page_number) - 1
        next_num = int(page_number) + 1
        last_page = products.page(1).paginator.num_pages
        number_of_products = len(list(products.object_list))
        return render(request, 'home/product_filter.html',
                      {'products': products, 'categories': categories, 'page_number': page_number,
                       'prev_num': prev_num,
                       'next_num': next_num,
                       'last_page': last_page,
                       'current_page': products.page(page_number).number,
                       'number_of_products': number_of_products})


class ProductDetailView(View):
    def get(self, request, slug):
        categories = Category.objects.filter(is_sub=False)
        product = get_object_or_404(Product, slug=slug)
        print(product.features.name)
        return render(request, 'home/detail.html', {'product': product, 'categories': categories})


class DiscountedProducts(View):
    def get(self, request):
        discounted_products = Product.objects.filter(discount__gt=20)
        return render(request, 'home/daredabe_discount.html', {'products': discounted_products})


class FavouriteProducts(View):
    def get(self, request):
        products = Product.objects.filter(available=True)
        favourite_products = products.order_by('-price')[:6]
        return render(request, 'home/daredabe_favourite.html', {'products': favourite_products})
