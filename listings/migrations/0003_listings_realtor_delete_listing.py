# Generated by Django 5.0.6 on 2024-08-14 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0002_listings_remove_listing_realtor"),
        ("realtors", "0002_realtors_delete_realtor"),
    ]

    operations = [
        migrations.AddField(
            model_name="listings",
            name="realtor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="realtors.realtors"
            ),
        ),
        migrations.DeleteModel(
            name="Listing",
        ),
    ]
