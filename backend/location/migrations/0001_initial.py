# Generated by Django 2.2.18 on 2021-02-05 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("task_profile", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MapLocation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("latitude", models.DecimalField(decimal_places=8, max_digits=12)),
                ("longitude", models.DecimalField(decimal_places=8, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name="TaskLocation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.TextField()),
                ("zip", models.CharField(max_length=6)),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasklocation_location",
                        to="location.MapLocation",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TaskerLocation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("latitude", models.DecimalField(decimal_places=8, max_digits=12)),
                ("longitude", models.DecimalField(decimal_places=8, max_digits=12)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                ("address", models.TextField(blank=True, null=True)),
                ("zip", models.CharField(blank=True, max_length=6, null=True)),
                (
                    "tasker",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="taskerlocation_tasker",
                        to="task_profile.TaskerProfile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomerLocation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("zip", models.CharField(max_length=6)),
                ("country", models.CharField(max_length=50)),
                (
                    "customer",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customerlocation_customer",
                        to="task_profile.CustomerProfile",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customerlocation_location",
                        to="location.MapLocation",
                    ),
                ),
            ],
        ),
    ]
