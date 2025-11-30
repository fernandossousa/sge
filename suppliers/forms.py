from django import forms
from . import models


class SupplierForm(forms.ModelForm):

    class Meta:
        model = models.Supplier
        fields = ['name', 'mail', 'phone', 'site', 'document_id', 'contact', 'contact_phone', 'address', 'city' , 'state' , 'zip_code', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Império da Sublimação'}),
            'mail': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: imperiodasublimacao@imperiodasublimacao'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: (11) 98888-0000'}),
            'site': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: https://imperiodasublimacao.com.br'}),
            'document_id': forms.TextInput(attrs={'class': 'form-control','maxlength': '20', 'placeholder': 'Ex: CPF: 000.000.000-00 | CNPJ: 12.345.678/0001-00'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Felipe'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: (11) 98888-0000'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Rua X, 100 - Jd. Novo Futuro'}),
            'city': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ex: Itupeva'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '2','placeholder': 'Ex: SP'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 00000-000'}), 
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ex: Informação adicional à este cadastro'}),
        }
        labels = {
            'name': 'Fornecedor',
            'mail': 'E-mail',
            'phone': 'Telefone',
            'site': 'Site/MediaSocial',
            'document_id': 'CPF/CNPJ',
            'contact': 'Vendedor',
            'contact_phone': 'Contato Vendedor',
            'address': 'Endereço',
            'city': 'Cidade',
            'state': 'Estado',
            'zip_code': 'CEP',
            'description': 'Descrição',
        }
