from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название продукта', help_text='Введите название продукта')
    description = models.TextField(verbose_name='Описание продукта', help_text='Введите описание продукта', blank=True)
    image = models.ImageField(upload_to='media/images', verbose_name='Фотография', help_text='Загрузите изображение продукта', blank=True)
    category = models.CharField(max_length=150, verbose_name='Название категории продукта', help_text='Введите название категории', blank=True)
    cost = models.IntegerField(verbose_name='цена за покупку', help_text='Введите цену', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', help_text='Введите дату создания', blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения', help_text='Введите дату последнего обновления', blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'description', 'category', 'cost']


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории', help_text='Введите название категории')
    description = models.TextField(verbose_name='Описание категории', help_text='Введите описание категории', blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name', 'description']
