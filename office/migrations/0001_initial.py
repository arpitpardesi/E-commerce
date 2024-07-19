# Generated by Django 4.1 on 2024-07-19 18:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                ("fName", models.CharField(max_length=50)),
                ("lName", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
            ],
        ),
    ]