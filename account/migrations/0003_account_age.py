# Generated by Django 4.1.2 on 2022-11-20 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='age',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
