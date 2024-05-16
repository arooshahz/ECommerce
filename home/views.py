from django.core.mail import send_mail
from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from Ecommerce import settings
from .models import Product, Category, OrderItem, Order, ProductImage
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
        if request.GET.get('search'):
            search_query = request.GET.get('search')
            products_list = products_list.filter(
                Q(description__icontains=search_query) |
                Q(name__icontains=search_query)
            )
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
        images = ProductImage.objects.filter(product=product)
        # print(product.features.name)
        return render(request, 'home/detail.html', {'product': product, 'categories': categories,
                                                    'images': images})


class DiscountedProducts(View):
    def get(self, request, page_number):
        categories = Category.objects.filter(is_sub=False)

        discounted_products = Product.objects.filter(discount__gt=20)
        products = Paginator(discounted_products, 9)
        prev_num = int(page_number) - 1
        next_num = int(page_number) + 1
        last_page = products.page(1).paginator.num_pages
        return render(request, 'home/special_offers.html',
                      {'products': products, 'categories': categories, 'page_number': page_number,
                       'prev_num': prev_num,
                       'next_num': next_num,
                       'last_page': last_page,
                       'current_page': products.page(page_number).number})


class FavouriteProducts(View):
    def get(self, request, page_number=1):
        categories = Category.objects.filter(is_sub=False)

        products = Product.objects.filter(available=True)
        favourite_products = products.order_by('-price')[:6]
        products = Paginator(favourite_products, 6)
        prev_num = int(page_number) - 1
        next_num = int(page_number) + 1
        last_page = products.page(1).paginator.num_pages
        return render(request, 'home/favourites.html',
                      {'products': products, 'categories': categories, 'page_number': page_number,
                       'prev_num': prev_num,
                       'next_num': next_num,
                       'last_page': last_page,
                       'current_page': products.page(page_number).number})


class AddToOrder(View):
    def post(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        order_id = request.session.get('order_id')

        if order_id:
            order = get_object_or_404(Order, id=order_id)
        else:
            order = Order.objects.create(
                name='', last_name='', company_name='', province='',
                City='', street='', apartment='', Postalcode='',
                phone_number='', email=''
            )
            request.session['order_id'] = order.id

        order_item, created = OrderItem.objects.get_or_create(
            order=order,
            product=product,
            defaults={'quantity': 1}
        )

        if not created:
            order_item.quantity += 1
            order_item.save()

        return redirect('home:product_detail', product.slug)


class ViewOrder(View):
    def get(self, request):
        order_id = request.session.get('order_id')
        if order_id:
            order = get_object_or_404(Order, id=order_id)
            order_items = OrderItem.objects.filter(order=order)
            # total = sum(item.get_total_item_price() for item in order_items)
        else:
            order_items = []
            # total = 0

        return render(request, 'home/cart.html', {'order_items': order_items})

    def delete(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        order_id = request.session.get('order_id')
        if order_id:
            order = get_object_or_404(Order, id=order_id)
            order_item = get_object_or_404(OrderItem, order=order, product=product)
            order_item.delete()  # Delete the order item
        return redirect('home:cart')


class CartDoneView(View):
    def get(self, request):
        return render(request, 'home/cart_done.html')


class CartCompletionView(View):
    def get(self, request):
        return render(request, 'home/cart_info.html')

    def post(self, request):
        order_id = request.session.get('order_id')
        if order_id:
            order = get_object_or_404(Order, id=order_id)
            order_items = OrderItem.objects.filter(order=order)
        else:
            order_items = []
            order = Order()

        order.name = request.POST['fname']
        order.last_name = request.POST['lname']
        order.company_name = request.POST['company']
        order.province = request.POST['province']
        order.City = request.POST['city']
        order.street = request.POST['street']
        order.apartment = request.POST['building']
        order.Postalcode = request.POST['post_code']
        order.phone_number = request.POST['mobile']
        order.email = request.POST['email']
        order.save()

        subject = 'New Order Received'
        order_items_details = "\n".join(
            [f"- {item.product.name}: {item.quantity} units" for item in order_items]
        )
        message = (
            f"New order received:\n\n"
            f"Name: {order.name} {order.last_name}\n"
            f"Company: {order.company_name}\n"
            f"Province: {order.province}\n"
            f"City: {order.City}\n"
            f"Street: {order.street}\n"
            f"Apartment: {order.apartment}\n"
            f"Postal Code: {order.Postalcode}\n"
            f"Phone Number: {order.phone_number}\n"
            f"Email: {order.email}\n"
            f"Order Items:\n{order_items_details}\n"
        )
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.ADMIN_EMAIL]

        # Send the email
        send_mail(subject, message, from_email, recipient_list)

        return redirect('home:cart_info')
