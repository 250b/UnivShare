# Generated by Django 4.2.3 on 2023-10-08 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='significant',
            field=models.CharField(blank=True, choices=[('유학생', '유학생'), ('전과생', '전과생'), ('편입생', '편입생'), ('외국인', '외국인'), ('교환학생', '교환학생'), ('복수전공생', '복수전공생'), ('부전공생', '부전공생'), ('휴학생', '휴학생')], max_length=10, null=True, verbose_name='특이사항'),
        ),
    ]