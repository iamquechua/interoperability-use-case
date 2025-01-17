# Generated by Django 5.1.4 on 2024-12-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Citizen",
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
                (
                    "citizen_number",
                    models.CharField(editable=False, max_length=10, unique=True),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("middle_name", models.CharField(blank=True, max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("Female", "Female"), ("Male", "Male")], max_length=10
                    ),
                ),
                ("phone_number", models.CharField(max_length=30)),
                ("address", models.CharField(max_length=100)),
            ],
        ),
    ]
