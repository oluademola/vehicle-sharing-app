"""
This contains admin view and customisation options
for the users module.
"""

from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    """
    Admin display and search options.
    """
    list_display = ('id', 'email', 'first_name', 'last_name',
                    'is_active', 'is_staff', 'is_superuser', 'last_login')
    search_fields = ('email',)
    readonly_fields = ('id',)
