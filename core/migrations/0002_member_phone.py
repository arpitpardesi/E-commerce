# Generated by Django 4.1 on 2024-06-20 19:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="phone",
            field=models.IntegerField(null=True),
        ),
    ]