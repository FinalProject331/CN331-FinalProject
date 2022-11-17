# Generated by Django 4.1.2 on 2022-11-17 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0008_alter_shop_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='addshop',
            name='shop_name',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='addshop',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]