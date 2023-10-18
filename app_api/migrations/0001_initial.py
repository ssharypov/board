# Generated by Django 4.2.4 on 2023-10-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Code",
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
                ("code_string", models.TextField(verbose_name="Код")),
                ("generation_time", models.DateTimeField(verbose_name="Когда создан")),
            ],
            options={
                "verbose_name": "Проверочный код",
                "verbose_name_plural": "Проверочные коды",
            },
        ),
    ]
