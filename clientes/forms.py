# ==================== forms.py ====================
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'cpf_cnpj', 'endereco', 'cidade', 'estado', 'cep']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'exemplo@email.com'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000'
            }),
            'cpf_cnpj': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '000.000.000-00 ou 00.000.000/0000-00'
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rua, número, bairro'
            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da cidade'
            }),
            'estado': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': '2',
                'placeholder': 'SP'
            }),
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00000-000'
            }),
        }
    
    def clean_cpf_cnpj(self):
        cpf_cnpj = self.cleaned_data.get('cpf_cnpj')
        # Remove caracteres especiais
        cpf_cnpj_limpo = ''.join(filter(str.isdigit, cpf_cnpj))
        
        # Verifica se é CPF (11 dígitos) ou CNPJ (14 dígitos)
        if len(cpf_cnpj_limpo) not in [11, 14]:
            raise forms.ValidationError('CPF deve ter 11 dígitos ou CNPJ deve ter 14 dígitos.')
        
        return cpf_cnpj
    
    def clean_estado(self):
        estado = self.cleaned_data.get('estado')
        if estado:
            return estado.upper()
        return estado
