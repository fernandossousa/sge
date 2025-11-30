from django import forms
from django.core.exceptions import ValidationError
from . import models
from .models import Outflow
from costumers.models import Costumer


class OutflowForm(forms.ModelForm):
    costumer = forms.ModelChoiceField(
        queryset=Costumer.objects.all(),
        required=False,
        label="Cliente",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    

    class Meta:
        model = models.Outflow
        #fields = ['product', 'quantity', 'description']
        fields = ["costumer", "product", "description", "quantity", "value"]
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise ValidationError(
                f'A quantidade disponível em estoque para o produto {product.title} é de {product.quantity} unidades.'
            )

        return quantity
