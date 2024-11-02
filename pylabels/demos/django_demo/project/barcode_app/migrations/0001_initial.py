# Generated by Django 5.1.2 on 2024-10-10 02:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LabelSpecification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(default="default", max_length=50, unique=True)),
                ("sheet_width", models.FloatField(default=210.0)),
                ("sheet_height", models.FloatField(default=297.0)),
                ("columns", models.IntegerField(default=2)),
                ("rows", models.IntegerField(default=6)),
                ("label_width", models.FloatField(default=96.0)),
                ("label_height", models.FloatField(default=42.0)),
                ("border", models.BooleanField(default=True)),
                ("row_gap", models.FloatField(blank=True, default=None, null=True)),
                ("column_gap", models.FloatField(blank=True, default=None, null=True)),
                ("top_margin", models.FloatField(default=21.0)),
                ("left_margin", models.FloatField(default=8.0)),
                ("right_margin", models.FloatField(default=8.0)),
                ("bottom_margin", models.FloatField(default=22.0)),
                ("left_padding", models.FloatField(default=2.0)),
                ("right_padding", models.FloatField(default=2.0)),
                ("top_padding", models.FloatField(default=2.0)),
                ("bottom_padding", models.FloatField(default=2.0)),
                ("corner_radius", models.IntegerField(default=0)),
                ("padding_radius", models.IntegerField(default=0)),
                ("page_description", models.CharField(max_length=250, null=True)),
                ("layout_description", models.CharField(max_length=250, null=True)),
                ("label_description", models.CharField(max_length=250, null=True)),
            ],
            options={
                "verbose_name": "Label Sheet Specification",
                "verbose_name_plural": "Label Sheet Specifications",
            },
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("subject_identifier", models.CharField(max_length=25)),
                (
                    "gender",
                    models.CharField(choices=[("M", "Male"), ("F", "Female")], max_length=5),
                ),
                ("clinic", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="LabelData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("reference", models.CharField(max_length=10)),
                ("relative_seq", models.CharField(max_length=15)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="barcode_app.subject"
                    ),
                ),
            ],
        ),
    ]
