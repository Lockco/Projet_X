# Generated by Django 4.1.5 on 2023-01-18 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="review",
            options={
                "ordering": ["time_created"],
                "verbose_name": "Review",
                "verbose_name_plural": "Toutes les reviews",
            },
        ),
    ]
