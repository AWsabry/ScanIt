# Generated by Django 2.2.28 on 2023-10-03 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories_and_products', '0003_auto_20230723_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, help_text='Insert Link From Firebase Storage', max_length=250),
        ),
    ]
