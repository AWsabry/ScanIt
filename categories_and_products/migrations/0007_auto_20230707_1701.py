# Generated by Django 2.2.28 on 2023-07-07 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories_and_products', '0006_subcategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='SubCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories_and_products.SubCategory'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='vendor_type',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
