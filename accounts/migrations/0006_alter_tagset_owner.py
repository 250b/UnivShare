# Generated by Django 4.2.3 on 2023-10-01 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_tagset_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagset',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagset_user', to=settings.AUTH_USER_MODEL, verbose_name='유저'),
        ),
    ]