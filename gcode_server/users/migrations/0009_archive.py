# Generated by Django 4.0.5 on 2022-06-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_commandparticipatingnow_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(db_index=True, max_length=7, verbose_name='Учебный год')),
                ('semester', models.CharField(choices=[('Осн', 'Осенний'), ('Вес', 'Весенний')], db_index=True, max_length=8)),
                ('musketeers', models.CharField(db_index=True, max_length=300)),
                ('duel', models.CharField(db_index=True, max_length=300)),
                ('groups', models.CharField(db_index=True, max_length=300)),
            ],
            options={
                'verbose_name': 'Архив',
            },
        ),
    ]
