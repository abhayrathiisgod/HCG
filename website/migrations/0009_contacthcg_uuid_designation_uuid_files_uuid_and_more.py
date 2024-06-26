# Generated by Django 5.0.6 on 2024-06-03 03:53

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0008_designation_delete_boardofdirector_delete_teams_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="contacthcg",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name="designation",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name="files",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name="frequentlyaskedquestions",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name="page",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name="socialmediaurl",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
