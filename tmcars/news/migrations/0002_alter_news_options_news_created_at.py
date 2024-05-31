# Generated by Django 4.2.1 on 2024-05-31 13:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="news",
            options={"verbose_name_plural": "News"},
        ),
        migrations.AddField(
            model_name="news",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
