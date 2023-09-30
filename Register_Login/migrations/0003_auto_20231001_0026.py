# Generated by Django 2.2.28 on 2023-09-30 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0002_profile_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=500)),
                ('message', models.TextField(blank=True, max_length=500, null=True)),
                ('subject', models.TextField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Newsletter',
        ),
    ]