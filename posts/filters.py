import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            'post_type': ['exact'],
            'post_tag': ['exact'],
            'author': ['exact'],
            'is_published': ['exact'],
        }
