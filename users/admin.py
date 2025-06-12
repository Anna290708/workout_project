from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    model = User
    list_display = ['email', 'username', 'is_active', 'is_staff']
    ordering = ['email']
