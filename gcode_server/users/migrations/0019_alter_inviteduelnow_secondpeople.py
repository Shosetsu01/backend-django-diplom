# Generated by Django 4.0.5 on 2022-06-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_inviteduelnow_remove_duelparticipatingnow_acceptduel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inviteduelnow',
            name='secondPeople',
            field=models.CharField(db_index=True, max_length=60, verbose_name='Участник №2'),
        ),
    ]