from django.db.models.signals import pre_save, post_delete, post_save
from django.dispatch import receiver
from .models import ContactUs, Designation, Files, OurInitiatives, NewsLetter, BulkEmail
from django.core.exceptions import ValidationError
from django.conf import settings
import re
from celery import shared_task
from .tasks import send_mail
#from redismail import settings

@receiver(pre_save, sender=OurInitiatives)
def pre_save_OurInitiatives(sender, instance, **kwargs):
    if instance.pk :
        old_instance = OurInitiatives.objects.get(pk=instance.pk)
        if instance.BannerImage != old_instance.BannerImage:
            old_instance.BannerImage.delete(save=False)
        if instance.box_icon1 != old_instance.box_icon1:
            old_instance.box_icon1e.delete(save=False)
        if instance.box_icon2 != old_instance.box_icon2:
            old_instance.box_icon2.delete(save=False)
        if instance.box_icon1 != old_instance.box_icon3:
            old_instance.box_icon3.delete(save=False)

@receiver(post_delete, sender=OurInitiatives)
def post_delete_OurInitiatives(sender, instance, **kwargs):
    instance.BannerImage.delete(save=False)
    instance.box_icon1.delete(save=False)
    instance.box_icon2.delete(save=False)
    instance.box_icon3.delete(save=False)

@receiver(pre_save, sender=ContactUs)
def validate_phone_number(sender, instance, **kwargs):
    phone_number = instance.PhoneNumber
    if phone_number:
        pattern = re.compile(r'^\+?1?\d{9,15}$')
        if not pattern.match(phone_number):
            raise ValidationError(f"Invalid phone number: {phone_number}")


@receiver(pre_save, sender=Designation)
def pre_save_Designationn(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Designation.objects.get(pk=instance.pk)
        if instance.image != old_instance.image:
            old_instance.image.delete(save=False)
    if instance.name and instance.image:
        ext = instance.image.name.split('.')[-1]
        instance.image.name = f"{instance.name}.{ext}"
    if instance.Is_Board_Member == False and instance.Is_Teams == False:
        raise ValidationError("Select either board member or Team memeber")

@receiver(post_delete, sender=Designation)
def post_delete_Designation(sender, instance, **kwargs):
    instance.image.delete(save=False)

@receiver(pre_save, sender=Files)
def pre_save_bulletin(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Files.objects.get(pk=instance.pk)
        if instance.file != old_instance.file:
            old_instance.file.delete(save=False)
        if instance.file_name and instance.file:
            ext = instance.file.name.split('.')[-1]
            instance.file.name = f"{instance.file_name}.{ext}"


@receiver(post_delete, sender=Files)
def post_delete_Files(sender, instance, **kwargs):
    instance.image.delete(save=False)


# send mail for cong subscribed to email list
    
@receiver(post_save, sender=NewsLetter)
def send_newsletter_confirmation_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Thank you for subscribing!'
        message = 'Welcome to our newsletter. You are now subscribed to receive updates.'
        recipient_list = [instance.email]
        sender_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, sender_email, recipient_list)


@receiver(post_save, sender=BulkEmail)
def send_bulk_email_task(sender, instance, created, **kwargs):
    print("created")
    if instance.message:
        print("inside msg")
        recipients = instance.recipients.values_list('email', flat=True)
        subject = instance.subject
        message = instance.message
        sender_email = settings.EMAIL_HOST_USER
        print("mail sent?")
        send_mail.delay(subject, message, sender_email, list(recipients))
        print("post mail sent?")

