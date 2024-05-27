# Generated by Django 4.2.1 on 2024-05-24 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=120)),
                ("image", models.ImageField(upload_to="posts")),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="CarCharacteristic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=30)),
                ("value", models.CharField(max_length=30)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cars.post"
                    ),
                ),
            ],
        ),
    ]
