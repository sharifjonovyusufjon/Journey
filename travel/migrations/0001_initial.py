# Generated by Django 5.1.7 on 2025-04-02 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Travel",
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
                ("travelTitle", models.CharField(max_length=400)),
                ("travelDesc", models.CharField(max_length=1000)),
                ("travelAddress", models.CharField(max_length=300)),
                ("travelImg", models.CharField(max_length=500)),
            ],
        ),
    ]
