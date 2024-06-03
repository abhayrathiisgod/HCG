# Generated by Django 5.0.6 on 2024-05-31 04:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobTypeName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='JobOpening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PositionName', models.CharField(max_length=255)),
                ('OpeningDate', models.DateField(blank=True, null=True)),
                ('Deadline', models.DateField(blank=True, null=True)),
                ('AboutTheRole', models.TextField(blank=True, null=True)),
                ('JobType', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vacancies.jobtype')),
            ],
        ),
    ]