# Generated by Django 4.1.3 on 2022-11-29 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Otify", "0002_complaint_user_delete_region"),
    ]

    operations = [
        migrations.CreateModel(
            name="Region",
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
                ("region", models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name="complaint",
            name="region",
            field=models.ManyToManyField(to="Otify.region"),
        ),
    ]
