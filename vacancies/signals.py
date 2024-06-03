from django.db.models.signals import pre_save, post_delete, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.core.mail import send_mail
import os
from .models import Proposal, Candidate
from django.conf import settings

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



# send email for application received and project successfully submitted -? post save
    
@receiver(post_save, sender=Candidate)
def send_job_applied_confirmation_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Thank you for applying!'
        message = f'Dear {instance.FirstName},\n\n' \
              f'Thank you for applying for the position of {instance.Position} with our company. ' \
              f'This email is to confirm that we have received your application. ' \
              f'We appreciate your interest in joining our team and will review your application carefully. ' \
              f'We will get back to you soon with further updates.\n\n' \
              f'Best regards,\nYour Company Name'
        recipient_list = [instance.Email]
        sender_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, sender_email, recipient_list)


@receiver(post_save, sender=Proposal)
def send_job_applied_confirmation_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Thank you for applying!'
        message = f'Dear {instance.FirstName},\n\n' \
              f'Thank you for applying project titlted {instance.ProjectName} with our company. ' \
              f'This email is to confirm that we have received your application. ' \
              f'We appreciate your interest in joining our team and will review your application carefully. ' \
              f'We will get back to you soon with further updates.\n\n' \
              f'Best regards,\nYour Company Name'
        recipient_list = [instance.Email]
        sender_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, sender_email, recipient_list)