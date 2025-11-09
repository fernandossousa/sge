from django import forms
from django.forms import inlineformset_factory
from .models import Product, ProductImage  # Agora ProductImage existe!
import os

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title', 
            'description', 
            'serie_number', 
            'brand', 
            'category', 
            'cost_price', 
            'selling_price', 
            'quantity',
            'color',
            'size',
            'type',
            'image'
        ]
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do produto'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descrição detalhada do produto'
            }),
            'serie_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de série único'
            }),
            'brand': forms.Select(attrs={
                'class': 'form-select'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'cost_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': '0.00'
            }),
            'selling_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': '0.00'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0'
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Azul, Vermelho, Preto'
            }),
            'size': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: P, M, G, GG'
            }),
            'type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Camiseta, Calça'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Limitar a 5MB
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError('O arquivo não pode ter mais de 5MB!')
            
            # Validar formato
            valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
            ext = os.path.splitext(image.name)[1].lower()
            if ext not in valid_extensions:
                raise forms.ValidationError('Formato não suportado. Use JPG, PNG, GIF ou WebP.')
        
        return image


class ProductImageForm(forms.ModelForm):
    """Formulário para cada imagem da galeria"""
    class Meta:
        model = ProductImage
        fields = ['image', 'order']
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'order': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'value': 0
            })
        }

# Formset para múltiplas imagens
ProductImageFormSet = inlineformset_factory(
    Product,           # Modelo pai
    ProductImage,      # Modelo filho
    form=ProductImageForm,
    extra=3,           # 3 formulários vazios extras
    can_delete=True,   # Permitir deletar
    max_num=10         # Máximo de 10 imagens
)