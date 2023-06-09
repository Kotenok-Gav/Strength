# Generated by Django 4.2 on 2023-04-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rockets_bdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Название проекта', max_length=200, null=True)),
                ('start_rocket', models.PositiveSmallIntegerField(help_text='Введите 0, если старт подводный,     1 - наземный', null=True)),
                ('t', models.DecimalField(decimal_places=3, help_text='с точностью до тысячных', max_digits=6, verbose_name='Время выхода ракеты из контейнера в секундах')),
                ('data_added', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
