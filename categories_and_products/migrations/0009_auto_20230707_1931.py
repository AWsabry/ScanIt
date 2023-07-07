# Generated by Django 2.2.28 on 2023-07-07 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories_and_products', '0008_remove_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, upload_to='Gallery')),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories_and_products.Product')),
            ],
        ),
        migrations.DeleteModel(
            name='Poster',
        ),
    ]
