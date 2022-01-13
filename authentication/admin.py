from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'id')
    readonly_fields = ('id',)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
