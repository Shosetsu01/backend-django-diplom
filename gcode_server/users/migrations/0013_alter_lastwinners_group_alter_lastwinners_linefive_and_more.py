# Generated by Django 4.0.5 on 2022-06-18 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_commandparticipatingnow_fifthpeople_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastwinners',
            name='group',
            field=models.CharField(db_index=True, max_length=60, unique=True, verbose_name='Уч. группа (для мушкетеров)'),
        ),
        migrations.AlterField(
            model_name='lastwinners',
            name='lineFive',
            field=models.CharField(blank=True, db_index=True, max_length=30, null=True, verbose_name='уч. №5 или побед. №5 (для мушкетеров/дуэлей)'),
        ),
        migrations.AlterField(
            model_name='lastwinners',
            name='lineFour',
            field=models.CharField(blank=True, db_index=True, max_length=30, null=True, verbose_name='уч. №4 или побед. №4 (для мушкетеров/дуэлей)'),
        ),
        migrations.AlterField(
            model_name='lastwinners',
            name='lineOne',
            field=models.CharField(db_index=True, max_length=30, verbose_name='уч. №1 или побед. №1 (для мушкетеров/дуэлей)'),
        ),
        migrations.AlterField(
            model_name='lastwinners',
            name='lineThree',
            field=models.CharField(blank=True, db_index=True, max_length=30, null=True, verbose_name='уч. №3 или побед. №3 (для мушкетеров/дуэлей)'),
        ),
        migrations.AlterField(
            model_name='lastwinners',
            name='lineTwo',
            field=models.CharField(blank=True, db_index=True, max_length=30, null=True, verbose_name='уч. №2 или побед. №2 (для мушкетеров/дуэлей)'),
        ),
    ]
