from django.shortcuts import render, get_object_or_404
from django.views import View
import random

from accounts.forms import UserRegistrationForm


class UserRegistrationView(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        # products = Product.objects.filter(available=True)
        return render(request, 'accounts/base.html', )

        form = self.form_class
        return render(request, self.template_name, {'form': form})
