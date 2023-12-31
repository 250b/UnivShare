# Generated by Django 4.2.3 on 2023-11-05 06:02

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_user_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=128, verbose_name='이름')),
                ('profile', models.ImageField(upload_to='', verbose_name='프로필 이미지')),
            ],
            options={
                'verbose_name': '프로필 이미지',
                'verbose_name_plural': '프로필 이미지',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users_profile', to='accounts.profile'),
        ),
    ]
