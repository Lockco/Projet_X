# Generated by Django 4.1.5 on 2023-01-21 06:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tickets", "0001_initial"),
        ("reviews", "0004_alter_review_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="ticket",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="tickets.ticket",
            ),
            preserve_default=False,
        ),
    ]