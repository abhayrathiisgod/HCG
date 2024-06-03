from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.safestring import mark_safe
import uuid
from django_ckeditor_5.fields import CKEditor5Field

class Designation(models.Model):
    class Meta:
        verbose_name = "Designation"
        verbose_name_plural = "1. Designations"
    uuid = models.UUIDField(default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='designations', default=None, blank=True, null=True, validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])])
    
    Is_Board_Member = models.BooleanField(default=False)
    Is_Teams = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name) + ' ' + str(self.designation)  
    

class OurInitiatives(models.Model):
    class Meta:
        verbose_name = "Our Inititatives"
        verbose_name_plural = "2. Our Inititatives"
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    PioneeringProjects_title = models.TextField(blank=True, null=True)
    FoundedYear = models.IntegerField()
    Projects = models.IntegerField()
    Communitites = models.CharField(max_length=255, blank=True, null=True )
    Volunteers = models.CharField(max_length=255, blank=True, null=True)
    BannerImage = models.ImageField(upload_to='banners/OurInitiatives', default=None, blank=True, null=True, validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])])
    box_title1 = models.CharField(max_length=255, blank=True, null=True)
    box_text1 = models.TextField(blank=True, null=True)
    box_icon1 = models.ImageField(upload_to='icons/', default=None, blank=True, null=True, validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])])
    box_title2 = models.CharField(max_length=255, blank=True, null=True)
    box_text2 = models.TextField(blank=True, null=True)
    box_icon2 = models.ImageField(upload_to='icons/', default=None, blank=True, null=True, validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])])
    box_title3 = models.CharField(max_length=255, blank=True, null=True)
    box_text3 = models.TextField(blank=True, null=True)
    box_icon3 = models.ImageField(upload_to='icons/', default=None, blank=True, null=True, validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])])

    def __str__(self) -> str:
        return "Our Initiatives Page"

    def image_preview(self):
        preview_html = ''
        if self.BannerImage:
            preview_html += '<h1>Banner Image</h1> <br> <img src="{0}" width="250" height="250" /><br><br>'.format(self.BannerImage.url)
        if self.box_icon1:
            preview_html += '<h1>Box Image 1</h1> <br> <img src="{0}" width="250" height="250" /><br><br>'.format(self.box_icon1.url)
        if self.box_icon2:
            preview_html += ' <h1>Box Image 2</h1> <br> <img src="{0}" width="250" height="250" /><br><br>'.format(self.box_icon2.url)
        if self.box_icon3:
            preview_html += '<h1>Box Image 3</h1> <br> <img src="{0}" width="250" height="250" /><br><br>'.format(self.box_icon3.url)

        if preview_html:
            return mark_safe(preview_html)
        else:
            return '(No images)'

class ContactHcg(models.Model):
    class Meta:
        verbose_name = "Contact HCG Information"
        verbose_name_plural = "3. Contact HCG Information"
    uuid = models.UUIDField(default = uuid.uuid4,editable = False)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    google_map_url = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return "Contact HCG"
    

class ContactUs(models.Model):
    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "4. Contact Us"
    FullName = models.CharField(max_length=255, blank=True, null=True)
    Email = models.EmailField(blank=True, null=True, unique=True)
    PhoneNumber = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Subject = models.TextField(blank=True, null=True)
    Message = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.FullName

class NewsLetter(models.Model):
    class Meta:
        verbose_name = "News letter"
        verbose_name_plural = "5. News letters"
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.email


class FrequentlyAskedQuestions(models.Model):
    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "6. FAQS"
    uuid = models.UUIDField(default = uuid.uuid4,editable = False)
    question =  models.CharField(max_length=255, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.question
    

class SocialMediaURL(models.Model):
    class Meta:
        verbose_name = "Social Media URL"
        verbose_name_plural = "7. Social Media URL"
    SocialMedia = (
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
        ('youtube', 'YouTube'),
    )
    uuid = models.UUIDField(default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=255, choices=SocialMedia)
    url = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    

class Page(models.Model):
    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "8. Pages"
    page_type = (
        ('about', 'About HCG'),
        ('mission', 'Mission and Vision'),
        ('Introduction', 'Introduction'),
    )
    uuid = models.UUIDField(default = uuid.uuid4,editable = False)
    page_name = models.CharField(max_length=255, choices=page_type)
    title = models.CharField(max_length=255, blank=True, null=True)
    text = CKEditor5Field('Text', config_name='extends')


class Files(models.Model):
    class Meta:
        verbose_name = "File"
        verbose_name_plural = "9 Files"
    file_type = (
        ('Privacy Policy', 'Privacy Policy'),
        ('Terms and Conditions', 'Terms of Service'),
    )
    uuid = models.UUIDField(default = uuid.uuid4,editable = False)
    file_name = models.CharField(max_length=255, choices=file_type)
    file = models.FileField(upload_to='files/', default=None, blank=True, null=True, validators=[
            FileExtensionValidator(allowed_extensions=["pdf"])])
    
    def __str__(self) -> str:
        return self.file_name
