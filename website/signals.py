from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import ContactUs, Designation, Files, OurInitiatives
from django.core.exceptions import ValidationError
import re

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