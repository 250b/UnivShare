# Generated by Django 4.2.3 on 2023-10-08 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_tagset_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='number',
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.CharField(choices=[('한국어문학부', '한국어문학부'), ('영어영문학부', '영어영문학부'), ('중국학부', '중국학부'), ('한국역사학과', '한국역사학과'), ('행정학과', '행정학과'), ('행정관리학과', '행정관리학과'), ('정치외교학과', '정치외교학과'), ('사회학과', '사회학과'), ('미디어광고학부', '미디어광고학부'), ('교육학과', '교육학과'), ('러시아유라시아학과', '러시아유라시아학과'), ('일본학과', '일본학과'), ('법학부', '법학부'), ('기업융합법학과', '기업융합법학과'), ('법학부', '법학부'), ('국제통상학과', '국제통상학과'), ('경영학부', '경영학부'), ('기업경영학부', '기업경영학부'), ('경영정보학부', '경영정보학부'), ('KMU KIBS', 'KMU KIBS'), ('재무금융회계학부', '재무금융회계학부'), ('AI빅데이터융합경영학과', 'AI빅데이터융합경영학과'), ('신소재공학부', '신소재공학부'), ('기계공학부', '기계공학부'), ('건설시스템공학부', '건설시스템공학부'), ('전자공학부', '전자공학부'), ('소프트웨어학부', '소프트웨어학부'), ('인공지능학부', '인공지능학부'), ('자동차공학과', '자동차공학과'), ('자동차IT융합학과', '자동차IT융합학과'), ('산림환경시스템학과', '산림환경시스템학과'), ('임산생명공학과', '임산생명공학과'), ('나노전자물리학과', '나노전자물리학과'), ('응용화학부', '응용화학부'), ('식품영양학과', '식품영양학과'), ('정보보안암호수학과', '정보보안암호수학과'), ('바이오발효융합학과', '바이오발효융합학과'), ('건축학부', '건축학부'), ('공업디자인학과', '공업디자인학과'), ('시각디자인학과', '시각디자인학과'), ('금속공예학과', '금속공예학과'), ('도자공예학과', '도자공예학과'), ('의상디자인학과', '의상디자인학과'), ('공간디자인학과', '공간디자인학과'), ('영상디자인학과', '영상디자인학과'), ('자동차운송디자인학과', '자동차운송디자인학과'), ('AI디자인학과', 'AI디자인학과'), ('음악학부', '음악학부'), ('미술학부', '미술학부'), ('공연예술학부', '공연예술학부'), ('스포츠교육학과', '스포츠교육학과'), ('스포츠산업레저학과', '스포츠산업레저학과'), ('스포츠건강재활학과', '스포츠건강재활학과'), ('미래모빌리티학과', '미래모빌리티학과'), ('교양대학', '교양대학'), ('인문기술융합학부', '인문기술융합학부')], max_length=20, null=True, verbose_name='학과'),
        ),
        migrations.AddField(
            model_name='user',
            name='grade',
            field=models.CharField(choices=[('1학년', '1학년'), ('2학년', '2학년'), ('3학년', '3학년'), ('4학년', '4학년'), ('5학년', '5학년'), ('졸업생', '졸업생'), ('기타', '기타')], max_length=10, null=True, verbose_name='학년'),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=6, null=True, verbose_name='닉네임'),
        ),
        migrations.AddField(
            model_name='user',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=100, null=True, verbose_name='평점'),
        ),
        migrations.AddField(
            model_name='user',
            name='significant',
            field=models.CharField(choices=[('유학생', '유학생'), ('전과생', '전과생'), ('편입생', '편입생'), ('외국인', '외국인'), ('교환학생', '교환학생'), ('복수전공생', '복수전공생'), ('부전공생', '부전공생'), ('휴학생', '휴학생')], max_length=10, null=True, verbose_name='특이사항'),
        ),
        migrations.AddField(
            model_name='user',
            name='student_number',
            field=models.BinaryField(max_length=10, null=True),
        ),
    ]