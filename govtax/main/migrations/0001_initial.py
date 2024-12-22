# Generated by Django 5.1.4 on 2024-12-22 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Taxpayer",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("Female", "Female"), ("Male", "Male")], max_length=10
                    ),
                ),
                ("phone", models.CharField(max_length=30)),
                ("home_address", models.CharField(max_length=100)),
                (
                    "total_tax_contribution",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
        ),
    ]