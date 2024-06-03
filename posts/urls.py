from django.urls import path
from .views import PostTypeViewSet, PostViewSet, AuthorViewSet, FeaturedBlogViewSet, PostTagViewSet


urlpatterns = [
    path('posttypes/', PostTypeViewSet.as_view({'get':'list'}), name='posttypes'),
    path('posttypes/<str:uuid>/', PostTypeViewSet.as_view({'get':'retrieve'}), name='posttype-detail'),

    path('posttags/', PostTagViewSet.as_view({'get':'list'}), name='posttags'),
    path('posttags/<str:uuid>/', PostTagViewSet.as_view({'get':'retrieve'}), name='posttags-detail'),

    path('posts/', PostViewSet.as_view({'get':'list'}), name='posts'),
    path('posts/<str:uuid>/', PostViewSet.as_view({'get':'retrieve'}), name='post-detail'),

    path('authors/', AuthorViewSet.as_view({'get':'list'}), name='authors'),
    path('authors/<str:uuid>/', AuthorViewSet.as_view({'get':'retrieve'}), name='author-detail'),
    
    path('featuredblogs/', FeaturedBlogViewSet.as_view({'get':'list'}), name='featuredblogs'),
]