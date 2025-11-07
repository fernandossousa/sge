# ==================== admin.py ====================
from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'telefone', 'cpf_cnpj', 'cidade', 'ativo', 'data_cadastro']
    list_filter = ['ativo', 'estado', 'data_cadastro']
    search_fields = ['nome', 'email', 'cpf_cnpj', 'telefone']
    list_per_page = 25
    ordering = ['-data_cadastro']

    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'email', 'telefone', 'cpf_cnpj')
        }),
        ('Endereço', {
            'fields': ('endereco', 'cidade', 'estado', 'cep')
        }),
        ('Status', {
            'fields': ('ativo',)
        }),
    )
