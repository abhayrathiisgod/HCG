# Generated by Django 5.0.6 on 2024-06-03 03:53

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0003_alter_author_options_alter_featuredblogs_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name="post",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name="posttag",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name="posttype",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
