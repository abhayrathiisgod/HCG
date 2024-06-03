from django.shortcuts import render
from .serializers import AuthorSerializer,PostListSerializer, PostTagSerializer, PostSerializer, PostTypeSerializer, FeaturedBlogSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Author, PostTag, Post, PostType, FeaturedBlogs
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter
from rest_framework.filters import OrderingFilter

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'uuid'

class PostTagViewSet(ModelViewSet):
    queryset = PostTag.objects.all()
    serializer_class = PostTagSerializer
    lookup_field = 'uuid'

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    lookup_field = 'uuid'
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = PostFilter
    ordering_fields = ['published_on',]

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        if self.action == 'retrieve':
            return PostSerializer
        return super().get_serializer_class()
    

class PostTypeViewSet(ModelViewSet):
    queryset = PostType.objects.all()
    serializer_class = PostTypeSerializer
    lookup_field = 'uuid'

class FeaturedBlogViewSet(ModelViewSet):
    queryset = FeaturedBlogs.objects.all()
    serializer_class = FeaturedBlogSerializer
    lookup_field = 'uuid'
