# Generated by Django 4.1.5 on 2023-04-14 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("organisation", "0002_organisations_api_key_organisations_terms_conditions"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="user",
            unique_together={("email", "organisation")},
        ),
        migrations.AddField(
            model_name="userprofiles",
            name="department",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_departments",
                to="organisation.departments",
            ),
        ),
    ]
