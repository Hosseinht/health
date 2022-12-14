# Generated by Django 4.1 on 2022-08-29 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("glucose", "0012_alter_glucose_glucose_level"),
    ]

    operations = [
        migrations.RenameField(
            model_name="glucose",
            old_name="recording_type",
            new_name="aufzeichnungstyp",
        ),
        migrations.RenameField(
            model_name="glucose",
            old_name="device",
            new_name="gerät",
        ),
        migrations.RenameField(
            model_name="glucose",
            old_name="device_timestamp",
            new_name="gerätezeitstempel",
        ),
        migrations.RenameField(
            model_name="glucose",
            old_name="serial_number",
            new_name="seriennummer",
        ),
        migrations.RemoveField(
            model_name="glucose",
            name="glucose_level",
        ),
        migrations.AddField(
            model_name="glucose",
            name="glukosewert",
            field=models.PositiveSmallIntegerField(
                default=1, help_text="Verlauf mg/dL"
            ),
            preserve_default=False,
        ),
    ]
