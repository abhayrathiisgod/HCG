# Generated by Django 5.0.6 on 2024-05-31 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0006_alter_candidate_email_alter_proposal_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={'verbose_name': 'Candidate', 'verbose_name_plural': '3. Candidates'},
        ),
        migrations.AlterModelOptions(
            name='jobopening',
            options={'verbose_name': 'Job Opening', 'verbose_name_plural': '2. Job Openings'},
        ),
        migrations.AlterModelOptions(
            name='jobtype',
            options={'verbose_name': 'Job Type', 'verbose_name_plural': '1. Job Types'},
        ),
        migrations.AlterModelOptions(
            name='proposal',
            options={'verbose_name': 'Proposal', 'verbose_name_plural': '4. Proposals'},
        ),
    ]
