# Generated by Django 5.0.6 on 2024-05-31 04:30

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobopening',
            name='JobRequirements',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Job Requirements'),
        ),
    ]
