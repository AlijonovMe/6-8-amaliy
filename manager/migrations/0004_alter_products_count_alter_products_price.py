# Generated by Django 5.1.3 on 2024-12-19 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_remove_categories_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='count',
            field=models.IntegerField(default=0, verbose_name='Soni'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Narxi'),
        ),
    ]