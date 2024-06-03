from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.utils.text import slugify
import os
from .models import Proposal, Candidate

@receiver(pre_save, sender=Proposal)
def rename_project_file(sender, instance, **kwargs):
    if instance.ProjectFile:
        file_extension = os.path.splitext(instance.ProjectFile.name)[1]
        new_filename = f"{slugify(instance.ProjectName)}{file_extension}"
        instance.ProjectFile.name = os.path.join('Proposals/', new_filename)

@receiver(post_delete, sender=Proposal)
def post_delete_Proposal(sender, instance, **kwargs):
    instance.ProjectFile.delete(save=False)

@receiver(pre_save, sender=Candidate)
def rename_cv_file(sender, instance, **kwargs):
    if instance.CV:
        file_extension = os.path.splitext(instance.CV.name)[1]
        new_filename = f"{slugify(instance.FirstName)}_{slugify(instance.LastName)}{file_extension}"
        instance.CV.name = os.path.join('CVs/', new_filename)

@receiver(post_delete, sender=Candidate)
def post_delete_Candidate(sender, instance, **kwargs):
    instance.CV.delete(save=False)