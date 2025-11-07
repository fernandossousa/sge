# ==================== urls.py ====================
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),
    path('novo/', views.criar_cliente, name='criar_cliente'),
    path('editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('deletar/<int:pk>/', views.deletar_cliente, name='deletar_cliente'),
    path('visualizar/<int:pk>/', views.visualizar_cliente, name='visualizar_cliente'),
]
