from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('all_products/<page_number>', views.ProductsView.as_view(), name='products'),
    path('discounted_products', views.DiscountedProducts.as_view(), name='discount_products'),
    path('category/<slug:slug>/<page_number>', views.CategoryView.as_view(), name='category'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail'),
    path('all_products/<int:min_price>/<int:max_price>/<page_number>', views.ProductBasedOnPrice.as_view(),
         name='product_price')
]
