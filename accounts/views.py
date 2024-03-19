from django.shortcuts import render, get_object_or_404
from django.views import View
# from .models import Product


class RegisterView(View):
    def get(self, request):
        # products = Product.objects.filter(available=True)
        return render(request, 'accounts/base.html', )

