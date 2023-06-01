# Generated by Django 4.2.1 on 2023-06-01 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdf', '0009_rockets_bdf_lg_1_rockets_bdf_lo_1_rockets_bdf_x_cy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rockets_bdf',
            name='N',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rockets_bdf',
            name='V_sredy',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]
