# Generated by Django 5.0.2 on 2024-04-03 10:58

import django.db.models.deletion
import store_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Supplier",
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
                ("username", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.IntegerField()),
            ],
            options={
                "db_table": "Supplier",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100)),
                ("stock", models.IntegerField()),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=15,
                        validators=[store_app.models.validate_check],
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store_app.supplier",
                    ),
                ),
            ],
            options={
                "db_table": "Product",
            },
        ),
    ]