from django.shortcuts import render
from .serializers import AuthorSerializer,PostListSerializer, PostTagSerializer, PostSerializer, PostTypeSerializer, FeaturedBlogSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Author, PostTag, Post, PostType, FeaturedBlogs
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import action

class AuthorViewSet(ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'uuid'

class PostTagViewSet(ReadOnlyModelViewSet):
    queryset = PostTag.objects.all()
    serializer_class = PostTagSerializer
    lookup_field = 'uuid'

class PostViewSet(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    lookup_field = 'uuid'
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = PostFilter
    ordering_fields = ['published_on']
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        if self.action == 'retrieve':
            return PostSerializer
        return super().get_serializer_class()
    
    @action(detail=False, methods=['GET'], name='get-related-posts', url_path='get-related')
    def get_related(self, request, *args, **kwargs):
        tag = request.query_params.get('tag_id')
        tag_instance = PostTag.objects.filter(uuid=tag).first()

        if not tag_instance:
            return Response({'message': 'Provide a valid tag'}, status=status.HTTP_404_NOT_FOUND)

        self.queryset = self.queryset.filter(post_tag=tag_instance)
        return self.list(request)

class PostTypeViewSet(ReadOnlyModelViewSet):
    queryset = PostType.objects.all()
    serializer_class = PostTypeSerializer
    lookup_field = 'uuid'

class FeaturedBlogViewSet(ReadOnlyModelViewSet):
    queryset = FeaturedBlogs.objects.all()
    serializer_class = FeaturedBlogSerializer
    lookup_field = 'uuid'


