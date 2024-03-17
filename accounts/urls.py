from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register', views.UserRegistrationView.as_view(), name='register'),
    # path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail')
]
