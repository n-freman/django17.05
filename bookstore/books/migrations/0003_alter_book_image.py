# Generated by Django 4.1.5 on 2024-06-21 13:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_book_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="books"),
        ),
    ]