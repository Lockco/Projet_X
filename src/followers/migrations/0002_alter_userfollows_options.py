# Generated by Django 4.1.5 on 2023-01-19 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("followers", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userfollows",
            options={
                "ordering": ["user"],
                "verbose_name": "Follower",
                "verbose_name_plural": "Tous les followers",
            },
        ),
    ]
