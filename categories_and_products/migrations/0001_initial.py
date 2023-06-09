# Generated by Django 2.2.28 on 2023-04-14 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=250, unique=True)),
                ('category_slug', models.SlugField(blank=True, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Categories')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=250, null=True)),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('Longitude', models.FloatField(blank=True, default=0, null=True)),
                ('Latitude', models.FloatField(blank=True, default=0, null=True)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, unique=True)),
                ('background_image', models.ImageField(blank=True, upload_to='Mobile_Poster')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True, unique=True)),
                ('vendor_slug', models.SlugField(unique=True)),
                ('number_of_branches', models.IntegerField(blank=True, default=1, null=True)),
                ('logo_image', models.ImageField(blank=True, upload_to='Vendors')),
                ('background_image', models.ImageField(blank=True, upload_to='Vendors')),
                ('Longitude', models.FloatField(blank=True, default=0, null=True)),
                ('Latitude', models.FloatField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('locations', models.ManyToManyField(blank=True, to='categories_and_products.Location')),
            ],
            options={
                'verbose_name_plural': 'Vendors',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('ArabicName', models.CharField(blank=True, max_length=250, null=True)),
                ('product_slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('Most_Popular', models.BooleanField(default=False)),
                ('New_Products', models.BooleanField(default=False)),
                ('Best_Offer', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories_and_products.Category')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories_and_products.Vendor')),
            ],
        ),
    ]
