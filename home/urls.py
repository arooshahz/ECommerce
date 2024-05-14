from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('all_products/<page_number>', views.ProductsView.as_view(), name='products'),
    path('discounted_products/<page_number>', views.DiscountedProducts.as_view(), name='discount_products'),
    path('favourite_products/<page_number>', views.FavouriteProducts.as_view(), name='favourite_products'),
    path('category/<slug:slug>/<page_number>', views.CategoryView.as_view(), name='category'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail'),
    path('all_products/<int:min_price>/<int:max_price>/<page_number>', views.ProductBasedOnPrice.as_view(),
         name='product_price'),
    path('add_order/<slug:slug>', views.AddToOrder.as_view(), name='add_order'),
    path('order_detail/<slug:slug>', views.ViewOrder.as_view(), name='order_detail'),
]
