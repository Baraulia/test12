from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    class Meta:
        ordering=('name',)
        verbose_name='Категория мебели'
        verbose_name_plural='Категории мебели'
    def __str__(self):
        return self.name
class Rubric(models.Model):
    category=models.ForeignKey(Category, related_name='rubric', on_delete=models.PROTECT)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
    def __str__(self):
        return self.name
class Type(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Тип мебели'
        verbose_name_plural = 'Типы мебели'
    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category, related_name='product', on_delete=models.PROTECT)
    rubric=models.ForeignKey(Rubric, related_name='product', on_delete=models.PROTECT)
    type=models.ForeignKey(Type, related_name='product', on_delete=models.PROTECT)
    name=models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug=models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True, verbose_name="Описание")
    image1=models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    image2=models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    image3=models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    price=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, verbose_name='Стоимость', db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('name',)
        index_together=(('id','slug'),)
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделия'





