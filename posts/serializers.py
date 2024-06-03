from rest_framework import serializers
from .models import Author, PostTag, Post, PostType, FeaturedBlogs


class AuthorSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Author
        exclude =['id']

class PostTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostTag
        exclude =['id']

class PostTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostType
        exclude =['id']

class PostListSerializer(serializers.ModelSerializer):

    post_type = PostTypeSerializer()
    post_tag = PostTagSerializer()
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = ('uuid','post_type', 'post_tag','author', 'title', 'short_summary','banner_image', 'is_published','read_time')

class PostSerializer(serializers.ModelSerializer):

    post_type = PostTypeSerializer()
    post_tag = PostTagSerializer()
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = ('uuid','post_type', 'post_tag', 'short_summary','author', 'title', 'banner_image', 'body', 'is_published', 'published_on','read_time')

class FeaturedBlogSerializer(serializers.ModelSerializer):

    BlogPost1 = PostListSerializer()
    BlogPost2 = PostListSerializer()
    BlogPost3 = PostListSerializer()
    BlogPost4 = PostListSerializer()

    class Meta:
        model = FeaturedBlogs
        exclude =['id']