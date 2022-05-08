# from django.contrib import admin
from auth_.models import AuthUser, Profile

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserAdmin(BaseUserAdmin):

    list_display = ('id', 'email', 'username', 'is_active', 'is_staff')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'username',)
    ordering = ('email',)


admin.site.register(AuthUser, UserAdmin)
admin.site.register(Profile)
admin.site.unregister(Group)

# Register your models here.
