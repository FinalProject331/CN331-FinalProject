# Generated by Django 4.1.2 on 2022-11-11 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_shop_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=300)),
            ],
        ),
    ]
