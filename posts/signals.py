from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import FeaturedBlogs, Author, Post

@receiver(pre_save, sender=FeaturedBlogs)
def check_unique_blog_posts(sender, instance, **kwargs):
    blog_posts = [instance.BlogPost1, instance.BlogPost2, instance.BlogPost3, instance.BlogPost4]
    blog_post_ids = [blog_post.id for blog_post in blog_posts]

    if len(blog_post_ids) != len(set(blog_post_ids)):
        raise ValidationError("All blog posts must be unique. Please ensure that BlogPost1, BlogPost2, BlogPost3, and BlogPost4 are different.")


@receiver(post_delete, sender=Author)
def post_delete_Designation(sender, instance, **kwargs):
    instance.profile_image.delete(save=False)

@receiver(pre_save, sender=Author)
def pre_save_Author(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Author.objects.get(pk=instance.pk)
        if instance.profile_image != old_instance.profile_image:
            old_instance.profile_image.delete(save=False)

@receiver(post_delete, sender=Post)
def post_delete_Designation(sender, instance, **kwargs):
    instance.banner_image.delete(save=False)

@receiver(pre_save, sender=Post)
def pre_save_Posts(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Post.objects.get(pk=instance.pk)
        if instance.banner_image != old_instance.banner_image:
            old_instance.banner_image.delete(save=False)