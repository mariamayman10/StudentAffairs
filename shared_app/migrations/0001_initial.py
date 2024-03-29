# Generated by Django 4.2.1 on 2023-05-24 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "student_id",
                    models.CharField(max_length=8, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=30)),
                ("gpa", models.DecimalField(decimal_places=2, max_digits=3)),
                ("level", models.IntegerField()),
                ("status", models.CharField(max_length=8)),
                ("department", models.CharField(max_length=2)),
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=11)),
                ("dob", models.DateField()),
                ("gender", models.CharField(max_length=6)),
            ],
        ),
    ]
