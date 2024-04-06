from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from .models import User


class UserAdmin(BaseUserAdmin):
    # form = UserChangeForm
    # add_form = UserCreationForm

    list_display = ('email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'last_login')}),
    )

    add_fieldsets = (
        (None, {'fields': ('phone_number', 'email', 'username', 'password')}),
    )

    search_fields = ('email',)
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
