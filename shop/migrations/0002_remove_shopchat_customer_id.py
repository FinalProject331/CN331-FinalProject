# Generated by Django 4.1.2 on 2022-11-19 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopchat',
            name='customer_id',
        ),
    ]