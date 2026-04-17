from django.urls import path
from . import views

urlpatterns = [
    path('', views.resident_list, name='resident_list'),
    path('nuevo/', views.resident_create, name='resident_create'),
    path('nuevo/<int:unit_pk>/', views.resident_create, name='resident_create_for_unit'),
    path('<int:pk>/', views.resident_detail, name='resident_detail'),
    path('<int:pk>/editar/', views.resident_edit, name='resident_edit'),
    path('<int:pk>/eliminar/', views.resident_delete, name='resident_delete'),
]
