# Generated by Django 4.2.2 on 2023-06-15 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdf', '0012_rockets_bdf_a1_rockets_bdf_a2_rockets_bdf_a3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rockets_bdf',
            name='tip_zakr_1',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rockets_bdf',
            name='tip_zakr_2',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rockets_bdf',
            name='tip_zakr_3',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rockets_bdf',
            name='tip_zakr_4',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rockets_bdf',
            name='tip_zakr_5',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rockets_bdf',
            name='a3',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='rockets_bdf',
            name='a4',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='rockets_bdf',
            name='a5',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=12, null=True),
        ),
    ]
