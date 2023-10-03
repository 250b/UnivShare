# Generated by Django 4.2.3 on 2023-10-01 05:58

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='이름')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='이메일')),
                ('password', models.CharField(max_length=256, verbose_name='패스워드')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='생년월일')),
                ('number', models.CharField(blank=True, max_length=28, null=True, verbose_name='전화번호')),
                ('profile', models.ImageField(blank=True, null=True, upload_to='', verbose_name='프로필 이미지')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화 여부')),
                ('is_staff', models.BooleanField(default=False, verbose_name='스태프 여부')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='최고 관리자 여부')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '유저 관리',
                'verbose_name_plural': '유저 관리',
            },
        ),
    ]