from django.db import models
from django.core.validators import FileExtensionValidator
from django_ckeditor_5.fields import CKEditor5Field
import uuid

class PostMeta(models.Model):
    class Meta:
        abstract = True

    uuid = models.UUIDField(default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    

class Author(models.Model):
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "1. Authors"
    uuid = models.UUIDField(default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=255)
    JobTitle = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='profile_images/', default=None, blank=True, null=True, validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])])
    
    def __str__(self):
        return self.name

class PostType(PostMeta):
    class Meta:
        verbose_name = "Post Type"
        verbose_name_plural = "2. Post Types"
    pass
    
class PostTag(PostMeta):
    class Meta:
        verbose_name = "Post Tag"
        verbose_name_plural = "3. Post Tags"
    pass

class Post(models.Model):

    class Meta:
        verbose_name = "Posts"
        verbose_name_plural = "4. Posts"
        ordering = ('-created_at',)

    uuid = models.UUIDField(default = uuid.uuid4,editable = False)
    post_type = models.ForeignKey(PostType, on_delete=models.PROTECT)
    post_tag = models.ForeignKey(PostTag, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    short_summary = models.CharField(max_length=255, help_text="A brief summary describing the content in 255 characters or less.", blank=True,null=True)
    banner_image = models.ImageField(upload_to='banners/', default=None, blank=True, null=True, validators=[
                              FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])])
    body = CKEditor5Field('Body', config_name='extends')
    is_published = models.BooleanField(default=False)
    published_on = models.DateTimeField(blank=True, null = True)
    read_time = models.IntegerField(blank=True, null = True)

    ## for backend admin read-only fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
         return str(self.post_type) +'->'+str(self.post_tag) + '->' + str(self.title)


class FeaturedBlogs(models.Model):

    class Meta:
        verbose_name = "Featured Blogs"
        verbose_name_plural = "5. Featured Blogs"

    uuid = models.UUIDField(default = uuid.uuid4,editable = False)
    BlogPost1 = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='featured_blog_post_1')
    BlogPost2 = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='featured_blog_post_2')
    BlogPost3 = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='featured_blog_post_3')
    BlogPost4 = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='featured_blog_post_4')

    def __str__(self):
        return f"{str(self.BlogPost1.title)}  {str(self.BlogPost2.title)} {str(self.BlogPost3.title)} {str(self.BlogPost4.title)}"