# Generated by Django 2.2.28 on 2023-10-03 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories_and_products', '0004_auto_20231003_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='images',
            field=models.CharField(blank=True, help_text='Insert Link From Firebase Storage', max_length=250),
        ),
    ]