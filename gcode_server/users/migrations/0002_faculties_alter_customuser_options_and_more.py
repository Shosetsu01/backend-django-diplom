# Generated by Django 4.0.5 on 2022-06-15 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculties',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(db_index=True, max_length=200)),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультеты',
            },
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['date_joined'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Is user is active', verbose_name='Is Active'),
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(db_index=True, max_length=200)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.faculties')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
    ]
