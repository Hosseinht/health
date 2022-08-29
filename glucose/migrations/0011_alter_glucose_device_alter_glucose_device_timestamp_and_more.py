# Generated by Django 4.1 on 2022-08-29 08:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        (
            "glucose",
            "0010_remove_glucose_aufzeichnungstyp_remove_glucose_gerät_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="glucose",
            name="device",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="glucose",
            name="device_timestamp",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="glucose",
            name="glucose_level",
            field=models.PositiveSmallIntegerField(help_text="Verlauf mg/dL"),
        ),
        migrations.AlterField(
            model_name="glucose",
            name="recording_type",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="glucose",
            name="serial_number",
            field=models.CharField(max_length=200),
        ),
    ]