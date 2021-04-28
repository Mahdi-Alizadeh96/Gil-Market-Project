from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import *
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm
    list_display = ('first_name', 'last_name', 'phone', 'email')
    list_filter = ('phone', 'is_active')
    fieldsets = (
        ('اطلاعات کاربر', {'fields': ('phone', 'password', 'first_name', 'last_name')}),
        ('دیگر اطلاعات شخصی', {'fields': ('email', 'address')}),
        ('مجوزها', {'fields': ('is_admin', 'is_active')})
    )

    add_fieldsets = (
        (None, {'fields': ('phone', 'first_name', 'last_name', 'password1', 'password2')}),
    )

    search_fields = ('first_name', 'last_name', 'phone')
    ordering = ('first_name', 'last_name', 'phone')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
