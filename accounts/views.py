from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
import random
from django.contrib import messages
from accounts.forms import UserRegistrationForm
from accounts.models import OtpCode


class UserRegistrationView(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        # products = Product.objects.filter(available=True)
        return render(request, 'accounts/base.html', )

        form = self.form_class
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            code = random.randint(1000, 9999)
            send_mail(
                "here is your code",
                code,
                "aroosha.ha@gmail.com",
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            OtpCode.objects.create(email=form.cleaned_data['email'], code=code)
            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone_number'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, 'we send you a code', 'success')
            # return redirect('accounts:verify_code')
        return render(request, self.template_name, {'form': form})