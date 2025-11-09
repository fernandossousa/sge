from django.db import models
from costumers.models import Costumer
from products.models import Product

class Outflow(models.Model):
    costumer = models.ForeignKey(
        Costumer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="outflows",
        verbose_name="Cliente"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="outflows",
        verbose_name="Produto"
    )

    quantity = models.PositiveIntegerField('Quantidade', default=1)
    value = models.DecimalField('Valor total', max_digits=10, decimal_places=2, default=0)
    description = models.TextField('Descrição', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.title} - {self.costumer}"

    def save(self, *args, **kwargs):
        # calcula valor automaticamente
        if self.value == 0 and hasattr(self.product, "selling_price"):
            self.value = self.product.selling_price * self.quantity
        super().save(*args, **kwargs)
