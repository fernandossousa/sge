from django.db import models
from PIL import Image
import os

class Product(models.Model):
    """Modelo de Produto - CAMPOS BÁSICOS"""
    title = models.CharField(max_length=200, verbose_name='Título')
    # description = models.CharField(blank=True, verbose_name='Título')
    # serie_number = models.CharField(max_length=200, unique=True, verbose_name='Número de Série')
    description = models.TextField(null=True, blank=True)
    serie_number = models.CharField(max_length=200, null=True, blank=True)    
    
    # ForeignKeys - ajuste conforme seu projeto
    brand = models.ForeignKey(
        'brands.Brand', 
        on_delete=models.PROTECT, 
        related_name='products', 
        verbose_name='Marca'
    )
    category = models.ForeignKey(
        'categories.Category', 
        on_delete=models.PROTECT, 
        related_name='products', 
        verbose_name='Categoria'
    )
    
    # Preços e Estoque
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço de Custo')
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço de Venda')
    quantity = models.IntegerField(default=0, verbose_name='Quantidade')
    
    # NOVOS CAMPOS: Cor, Tamanho, Tipo
    color = models.CharField(max_length=50, blank=True, null=True, verbose_name='Cor')
    size = models.CharField(max_length=20, blank=True, null=True, verbose_name='Tamanho')
    type = models.CharField(max_length=50, blank=True, null=True, verbose_name='Tipo')
    
    # IMAGEM PRINCIPAL
    image = models.ImageField(
        upload_to='products/', 
        blank=True, 
        null=True, 
        verbose_name='Imagem do Produto'
    )
    
    # Datas
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Redimensionar imagem se existir
        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)
            
            # Converter RGBA para RGB se necessário
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            
            # Redimensionar
            max_size = (800, 800)
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # Salvar otimizado
            img.save(img_path, format='JPEG', quality=85, optimize=True)


# NOVO MODELO - ADICIONE ESTE AGORA
class ProductImage(models.Model):
    """Modelo para galeria de imagens do produto"""
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='images',
        verbose_name='Produto'
    )
    image = models.ImageField(
        upload_to='products/gallery/', 
        verbose_name='Imagem'
    )
    order = models.IntegerField(default=0, verbose_name='Ordem')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'Imagem do Produto'
        verbose_name_plural = 'Imagens dos Produtos'
    
    def __str__(self):
        return f"Imagem de {self.product.title}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Redimensionar imagem da galeria
        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)
            
            # Converter RGBA para RGB
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            
            # Redimensionar
            max_size = (1200, 1200)
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # Salvar
            img.save(img_path, format='JPEG', quality=85, optimize=True)