# Generated by Django 5.1.4 on 2024-12-22 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Retiree",
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
                ("middle_name", models.CharField(max_length=100)),
                ("family_name", models.CharField(max_length=100)),
                ("birth_date", models.DateField()),
                (
                    "sex",
                    models.CharField(
                        choices=[("Female", "Female"), ("Male", "Male")], max_length=10
                    ),
                ),
                ("mobile_number", models.CharField(max_length=30)),
                ("physical_address", models.CharField(max_length=100)),
                (
                    "total_tax_contribution",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "yearly_pension_allowance",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
        ),
    ]
