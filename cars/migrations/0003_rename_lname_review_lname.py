# Generated by Django 4.1 on 2024-07-26 18:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0002_review"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="lname",
            new_name="lName",
        ),
    ]
