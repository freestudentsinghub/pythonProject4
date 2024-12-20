# Generated by Django 5.1.3 on 2024-12-18 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите заголовок', max_length=150, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, help_text='Введите описание', verbose_name='Содержимое')),
                ('preview', models.ImageField(blank=True, help_text='Загрузите изображение', upload_to='media/images', verbose_name='Фотография')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Введите дату создания', verbose_name='дата создания')),
                ('published', models.BooleanField(default=True, help_text='Укажите признак публикации', verbose_name='Признак публикации')),
                ('number_views', models.PositiveIntegerField(default=0, help_text='Укажите количество просмотров', verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ['title', 'content'],
            },
        ),
    ]
