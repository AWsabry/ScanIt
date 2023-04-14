# Generated by Django 2.2.28 on 2023-04-14 21:42

import categories_and_products.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories_and_products', '0003_auto_20230414_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='solid_File',
        ),
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, unique=True)),
                ('solid_File', models.FileField(upload_to=categories_and_products.models.get_upload_to)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories_and_products.Product')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories_and_products.Vendor')),
            ],
            options={
                'verbose_name_plural': '3dProducts',
            },
        ),
    ]
