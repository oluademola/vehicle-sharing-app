"""
Module contains basic auth filtering option for user.
"""

from django.shortcuts import redirect
from django.contrib import messages


def is_authenticated(view_func):
    """
    This method controls user access.
    """
    def wrapper_func(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            messages.error(request, 'You do not have access to this page.')
            return redirect("user_profile")
        return view_func(request, *args, **kwargs)
    return wrapper_func
