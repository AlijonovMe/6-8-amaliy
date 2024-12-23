# Generated by Django 5.1.3 on 2024-12-19 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nomi')),
                ('description', models.TextField(default="Ma'lumot qo'shilmadi.", verbose_name='Tavsifi')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Kategoriya ',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nomi')),
                ('price', models.IntegerField(verbose_name='Narxi')),
                ('count', models.IntegerField(verbose_name='Soni')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Surati')),
                ('published', models.BooleanField(default=False, verbose_name='Nashr etilgani')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.categories', verbose_name='Kategoriyasi')),
            ],
            options={
                'verbose_name': 'Mahsulot ',
                'verbose_name_plural': 'Mahsulotlar',
            },
        ),
    ]
