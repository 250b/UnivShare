# Generated by Django 4.2.3 on 2023-11-04 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='reason',
            field=models.CharField(choices=[('1', '비속어를 사용했어요.'), ('2', '약속 장소에 나오지 않았어요.'), ('3', '허위정보를 기재했어요.'), ('4', '기타 사유')], max_length=100, verbose_name='신고 사유'),
        ),
    ]
