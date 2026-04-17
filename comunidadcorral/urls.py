from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
import os


def setup_admin(request):
    secret = os.environ.get('SETUP_SECRET', '')
    if not secret or request.GET.get('key') != secret:
        return HttpResponse('Forbidden', status=403)
    from django.contrib.auth import get_user_model
    User = get_user_model()
    username = os.environ.get('ADMIN_USER', 'admin')
    password = os.environ.get('ADMIN_PASSWORD', '')
    if not password:
        return HttpResponse('ADMIN_PASSWORD no configurado', status=400)
    user, created = User.objects.get_or_create(username=username)
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.is_active = True
    user.email = os.environ.get('ADMIN_EMAIL', '')
    user.save()
    return HttpResponse(f'{"Creado" if created else "Actualizado"}: {username}')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('setup-admin/', setup_admin),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('accounts.urls')),
    path('units/', include('units.urls')),
    path('residents/', include('residents.urls')),
    path('organizations/', include('organizations.urls')),
]
