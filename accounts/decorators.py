from functools import wraps
from django.shortcuts import redirect


def tenant_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.organization and not request.user.is_superuser:
            return redirect('no_org')
        return view_func(request, *args, **kwargs)
    return wrapper
