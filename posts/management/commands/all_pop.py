import random
from django.core.management.base import BaseCommand
from faker import Faker
from posts.models import Post, PostType, PostTag, Author
from django.utils.timezone import make_aware
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Populate the Post model with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Assuming you have already created some PostType, PostTag, and Author instances
        post_types = list(PostType.objects.all())
        post_tags = list(PostTag.objects.all())
        authors = list(Author.objects.all())

        # Get the specific PostType and PostTag for 'initiative' and 'case'
        initiative_post_type = PostType.objects.filter(name='initiative').first()
        case_post_tag = PostTag.objects.filter(name='case').first()

        for _ in range(100):  # Number of posts to create
            post_type = random.choice(post_types)
            
            if post_type == initiative_post_type:
                post_tag = case_post_tag
            else:
                post_tag = random.choice(post_tags)
                
                # Ensure the post_tag is not 'case' if the post_type is not 'initiative'
                while post_tag == case_post_tag:
                    post_tag = random.choice(post_tags)

            author = random.choice(authors)
            title = fake.sentence(nb_words=6)
            short_summary = fake.text(max_nb_chars=255)
            body = fake.paragraph(nb_sentences=5)
            is_published = fake.boolean()
            published_on = make_aware(datetime.now() - timedelta(days=random.randint(1, 365))) if is_published else None
            read_time = random.randint(1, 20)
            created_at = make_aware(datetime.now() - timedelta(days=random.randint(1, 365)))
            updated_at = make_aware(datetime.now())

            post = Post(
                post_type=post_type,
                post_tag=post_tag,
                author=author,
                title=title,
                short_summary=short_summary,
                body=body,
                is_published=is_published,
                published_on=published_on,
                read_time=read_time,
                created_at=created_at,
                updated_at=updated_at,
            )

            post.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the Post model with fake data'))
