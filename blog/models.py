from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок', help_text='Введите заголовок')
    content = models.TextField(verbose_name='Содержимое', help_text='Введите описание', blank=True)
    preview = models.ImageField(upload_to='media/images', verbose_name='Фотография', help_text='Загрузите изображение', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания',help_text='Введите дату создания', blank=True)
    published = models.BooleanField(verbose_name="Признак публикации", help_text="Укажите признак публикации", default=True,)
    number_views = models.PositiveIntegerField(verbose_name="Количество просмотров", help_text="Укажите количество просмотров", default=0,)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'