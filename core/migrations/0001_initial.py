# Generated by Django 4.1b1 on 2022-06-27 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=256)),
                ("address", models.CharField(max_length=256)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="DataSheet",
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
                ("description", models.CharField(max_length=120)),
                ("historical_data", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Profession",
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
                ("description", models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name="Document",
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
                    "dtype",
                    models.CharField(
                        choices=[
                            ("PP", "Passport"),
                            ("ID", "Identity Card"),
                            ("OT", "Others"),
                        ],
                        max_length=2,
                    ),
                ),
                ("doc_number", models.CharField(max_length=50)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.customer"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="customer",
            name="data_sheet",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.datasheet",
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="professions",
            field=models.ManyToManyField(to="core.profession"),
        ),
    ]
