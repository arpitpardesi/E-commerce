# Generated by Django 4.1 on 2024-07-29 19:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("classroom", "0002_rename_teachers_teacher"),
    ]

    operations = [
        migrations.RenameField(
            model_name="teacher",
            old_name="lname",
            new_name="lName",
        ),
    ]