# Generated by Django 4.1 on 2022-08-29 04:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("glucose", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="glucose",
            name="aufzeichnungstyp",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="glucose",
            name="glukosewert",
            field=models.PositiveSmallIntegerField(
                default=0, help_text="Verlauf mg/dL"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="glucose",
            name="seriennummer",
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="glucose",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]