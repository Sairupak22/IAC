# Generated by Django 4.1.5 on 2023-04-01 10:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Departments",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                ("is_active", models.BooleanField(default=True)),
                ("organisation", models.CharField(max_length=100)),
                ("deleted_by", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Deleted at"
                    ),
                ),
                ("created_by", models.CharField(default="NULL", max_length=100)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                ("updated_by", models.CharField(default="NULL", max_length=100)),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("info", models.JSONField(blank=True, default=dict, null=True)),
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="GeneralSettings",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                ("is_active", models.BooleanField(default=True)),
                ("organisation", models.CharField(max_length=100)),
                ("deleted_by", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Deleted at"
                    ),
                ),
                ("created_by", models.CharField(default="NULL", max_length=100)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                ("updated_by", models.CharField(default="NULL", max_length=100)),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("info", models.JSONField(blank=True, default=dict, null=True)),
                ("country", models.CharField(default="IND", max_length=150)),
                ("currency", models.CharField(default="INR", max_length=150)),
                ("ccode", models.CharField(default="91", max_length=150)),
                ("timezone", models.CharField(default="IST", max_length=150)),
                ("dateformat", models.CharField(default="DD/MM/YYYY", max_length=150)),
                ("timeformat", models.CharField(default="HH:MM", max_length=150)),
                ("slot_duration", models.CharField(default="30", max_length=150)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Locations",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                ("is_active", models.BooleanField(default=True)),
                ("organisation", models.CharField(max_length=100)),
                ("deleted_by", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Deleted at"
                    ),
                ),
                ("created_by", models.CharField(default="NULL", max_length=100)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                ("updated_by", models.CharField(default="NULL", max_length=100)),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("info", models.JSONField(blank=True, default=dict, null=True)),
                ("name", models.CharField(max_length=100)),
                ("location", models.TextField(blank=True, null=True)),
                ("latitude", models.CharField(blank=True, max_length=100, null=True)),
                ("longitude", models.CharField(blank=True, max_length=100, null=True)),
                ("default", models.BooleanField(default=False)),
                (
                    "contact_person_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "contact_person_phone",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "address_one",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "address_two",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("state", models.CharField(blank=True, max_length=100, null=True)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("zipcode", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "ltype",
                    models.CharField(
                        choices=[("USER", "user"), ("ORGANISATION", "organisation")],
                        default="USER",
                        max_length=100,
                    ),
                ),
                ("ref_id", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Organisations",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                ("is_active", models.BooleanField(default=True)),
                ("organisation", models.CharField(max_length=100)),
                ("deleted_by", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Deleted at"
                    ),
                ),
                ("created_by", models.CharField(default="NULL", max_length=100)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                ("updated_by", models.CharField(default="NULL", max_length=100)),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("info", models.JSONField(blank=True, default=dict, null=True)),
                ("slug", models.CharField(max_length=150, unique=True)),
                ("name", models.CharField(max_length=150)),
                ("description", models.TextField(blank=True, null=True)),
                ("email", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("ccode", models.CharField(blank=True, max_length=10, null=True)),
                ("image", models.CharField(blank=True, max_length=150, null=True)),
                ("website", models.CharField(blank=True, max_length=150, null=True)),
                ("address", models.CharField(blank=True, max_length=150, null=True)),
                ("identifier", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "registration_id",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("language", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "instagram_url",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "twitter_url",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "linkedin_url",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "youtube_url",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="RolesPermissions",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                ("is_active", models.BooleanField(default=True)),
                ("organisation", models.CharField(max_length=100)),
                ("deleted_by", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Deleted at"
                    ),
                ),
                ("created_by", models.CharField(default="NULL", max_length=100)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                ("updated_by", models.CharField(default="NULL", max_length=100)),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("info", models.JSONField(blank=True, default=dict, null=True)),
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
                ("permissions", models.JSONField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="WorkingHours",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                ("is_active", models.BooleanField(default=True)),
                ("organisation", models.CharField(max_length=100)),
                ("deleted_by", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Deleted at"
                    ),
                ),
                ("created_by", models.CharField(default="NULL", max_length=100)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                ("updated_by", models.CharField(default="NULL", max_length=100)),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("info", models.JSONField(blank=True, default=dict, null=True)),
                ("days", models.CharField(max_length=100)),
                ("slots", models.JSONField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("USER", "user"),
                            ("ORGANISATION", "organisation"),
                            ("LOCATIONS", "locations"),
                        ],
                        default="USER",
                        max_length=100,
                    ),
                ),
                ("ref_id", models.CharField(max_length=100)),
            ],
            options={
                "unique_together": {("days", "ref_id")},
            },
        ),
    ]
