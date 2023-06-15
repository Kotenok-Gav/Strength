# Generated by Django 4.2.2 on 2023-06-15 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bdf', '0013_rockets_bdf_tip_zakr_1_rockets_bdf_tip_zakr_2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rockets_bdf',
            old_name='a1',
            new_name='L_kon_zakr_1',
        ),
        migrations.RenameField(
            model_name='rockets_bdf',
            old_name='a2',
            new_name='L_kon_zakr_2',
        ),
        migrations.RenameField(
            model_name='rockets_bdf',
            old_name='a3',
            new_name='L_kon_zakr_3',
        ),
        migrations.RenameField(
            model_name='rockets_bdf',
            old_name='a4',
            new_name='L_kon_zakr_4',
        ),
        migrations.RenameField(
            model_name='rockets_bdf',
            old_name='a5',
            new_name='L_kon_zakr_5',
        ),
        migrations.RemoveField(
            model_name='rockets_bdf',
            name='dl_1',
        ),
        migrations.RemoveField(
            model_name='rockets_bdf',
            name='dl_2',
        ),
        migrations.RemoveField(
            model_name='rockets_bdf',
            name='dl_3',
        ),
        migrations.RemoveField(
            model_name='rockets_bdf',
            name='nap_zak_1',
        ),
        migrations.RemoveField(
            model_name='rockets_bdf',
            name='nap_zak_2',
        ),
        migrations.RemoveField(
            model_name='rockets_bdf',
            name='nap_zak_3',
        ),
        migrations.RemoveField(
            model_name='rockets_bdf',
            name='zhestkost_opor_1',
        ),
        migrations.RemoveField(
            model_name='rockets_bdf',
            name='zhestkost_opor_2',
        ),
        migrations.RemoveField(
            model_name='rockets_bdf',
            name='zhestkost_opor_3',
        ),
    ]
