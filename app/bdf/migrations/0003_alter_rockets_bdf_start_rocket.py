# Generated by Django 4.2 on 2023-04-20 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdf', '0002_remove_rockets_bdf_data_added_remove_rockets_bdf_t'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rockets_bdf',
            name='start_rocket',
            field=models.CharField(help_text='Название проекта', max_length=200, null=True),
        ),
    ]
