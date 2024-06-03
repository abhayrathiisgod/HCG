from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import Author, PostTag, Post, PostType, FeaturedBlogs


class CustomAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False

class AuthorAdmin(CustomAdmin):
    list_display = ('name','JobTitle')
    list_display_links= ('name','JobTitle')
    search_fields = ('name','JobTitle')

class PostTagAdmin(CustomAdmin):
    actions = None
    list_display = ('name',)
    list_display_links= ('name',)
    search_fields = ('name',)

class PostTypeAdmin(CustomAdmin):
    actions = None
    list_display = ('name',)
    list_display_links= ('name',)
    search_fields = ('name',)

class PostAdmin(CustomAdmin):
    list_display = ('title','post_type','post_tag','author','is_published')
    list_display_links= ('title','post_type','post_tag','author','is_published')
    list_filter = ('post_type','author','post_tag','is_published')
    search_fields = ('title',)
    readonly_fields = ('created_at','updated_at')


admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Author)
admin.site.register(PostTag)
admin.site.register(Post, PostAdmin)
admin.site.register(PostType)
admin.site.register(FeaturedBlogs)