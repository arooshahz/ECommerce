from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('all_products/<page_number>', views.ProductsView.as_view(), name='products'),
    path('category/<slug:slug>', views.CategoryView.as_view(), name='category'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail')
]
