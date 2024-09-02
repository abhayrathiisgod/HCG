from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostTypeViewSet, PostViewSet, AuthorViewSet, FeaturedBlogViewSet, PostTagViewSet

router = DefaultRouter()
router.register(r'post-types', PostTypeViewSet, basename='posttype')
router.register(r'post-tags', PostTagViewSet, basename='posttag')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'featured-blogs', FeaturedBlogViewSet, basename='featuredblog')

urlpatterns = [
    path('', include(router.urls)),
]
