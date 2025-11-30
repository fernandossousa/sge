from django import forms
from . import models


class CostumerForm(forms.ModelForm):

    class Meta:
        model = models.Costumer
        fields = ['name', 'mail', 'phone', 'document_id', 'social_media', 'address', 'city' , 'state' , 'zip_code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: José da Silva'}),
            'mail': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ex: jose.silva@gmail.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ex: (11)98888-0000'}),
            'document_id': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ex: CPF: 000.000.000-00 | CNPJ: 12.345.678/0001-00'}),
            'social_media': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: @josedasilva | www.josedasilva.com.br'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Rua X, 100 - Jd. Novo Futuro'}),
            'city': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ex: Itupeva'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '2','placeholder': 'Ex: SP'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 00000-000'}),
        }
        labels = {
            'name': 'Nome',
            'mail': 'E-mail',
            'phone': 'Telefone',
            'document_id': 'CPF/CNPJ',
            'social_media': 'Site/MediaSocial',
            'address': 'Endereço',
            'city': 'Cidade',
            'state': 'Estado',
            'zip_code': 'CEP',
        }
