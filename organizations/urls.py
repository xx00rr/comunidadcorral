from django.urls import path
from . import views

urlpatterns = [
    path('', views.org_detail, name='org_detail'),
    path('editar/', views.org_edit, name='org_edit'),
]
