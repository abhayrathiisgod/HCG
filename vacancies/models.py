from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.core.validators import FileExtensionValidator
import uuid


class JobType(models.Model):
    class Meta:
        verbose_name = "Job Type"
        verbose_name_plural = "1. Job Types"
    uuid = models.UUIDField(default = uuid.uuid4,editable = False)
    JobTypeName = models.CharField(max_length=255)

    def __str__(self):
        return self.JobTypeName

class JobOpening(models.Model):
    class Meta:
        verbose_name = "Job Opening"
        verbose_name_plural = "2. Job Openings"

    uuid = models.UUIDField(default = uuid.uuid4,editable = False)
    PositionName = models.CharField(max_length=255)
    JobType = models.ForeignKey(JobType, on_delete= models.PROTECT)
    OpeningDate = models.DateField(blank=True, null = True)
    Deadline = models.DateField(blank=True, null = True)
    AboutTheRole = models.TextField(blank=True, null = True)
    JobRequirements = CKEditor5Field('Job Requirements', config_name='extends', blank=True, null = True)
    is_published = models.BooleanField(default=False)

    # read-only field 
    Created_at = models.DateTimeField(auto_now_add=True, blank=True, null = True)
    Updated_at = models.DateTimeField(auto_now=True, blank=True, null = True)

    def __str__(self):
        return self.PositionName

class Candidate(models.Model):

    class Meta:
        verbose_name = "Candidate"
        verbose_name_plural = "3. Candidates"

    uuid = models.UUIDField(default = uuid.uuid4,editable = False)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.EmailField(unique=True)
    PhoneNumber = models.CharField(max_length=100)
    Position = models.ForeignKey(JobOpening, on_delete= models.PROTECT)
    CV = models.FileField(upload_to='CVs/', default=None, validators=[
            FileExtensionValidator(allowed_extensions=["pdf"])], blank=True, null=True)
    
    # read-only field 
    Created_at = models.DateTimeField(auto_now_add=True, blank=True, null = True)
    Updated_at = models.DateTimeField(auto_now=True, blank=True, null = True)


    def __str__(self):
        return self.FirstName + self.LastName


class Proposal(models.Model):
    
    class Meta:
        verbose_name = "Proposal"
        verbose_name_plural = "4. Proposals"

    uuid = models.UUIDField(default = uuid.uuid4,editable = False)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.EmailField(unique=True)
    PhoneNumber = models.CharField(max_length=100)
    ProjectName = models.CharField(max_length=100)
    ProjectFile = models.FileField(upload_to='Proposals/', default=None, validators=[
            FileExtensionValidator(allowed_extensions=["pdf"])], blank=True, null=True)
    
    # read-only field 
    Created_at = models.DateTimeField(auto_now_add=True, blank=True, null = True)
    Updated_at = models.DateTimeField(auto_now=True, blank=True, null = True)

    def __str__(self):
        return self.ProjectName
