from django.contrib import admin
from website.models import ContactUs,BulkEmail, Page, Files, Designation, ContactHcg, OurInitiatives, NewsLetter, FrequentlyAskedQuestions, SocialMediaURL

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
    
class DesignationAdmin(CustomAdmin):
    list_display = ('name','designation','Is_Board_Member','Is_Teams')
    list_display_links = ('name','designation','Is_Board_Member','Is_Teams')
    list_filter = ('Is_Board_Member','Is_Teams')

class OurInitiativesAdmin(CustomAdmin):
    actions = None
    list_display = ('title',)
    list_display_links= ('title',)
    readonly_fields = ('image_preview',)

class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_display_links= ('email',)
    search_fields = ('email',)

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False
    
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('FullName',)
    list_display_links= ('FullName',)
    search_fields = ('FullName',)

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False
    
class PageAdmin(CustomAdmin):
    list_display = ('page_name',)
    list_display_links= ('page_name',)
    search_fields = ('title',)

class ContactHcgAdmin(admin.ModelAdmin):
    list_display = ('email','phone','location')
    list_display_links= ('email','phone','location')
    
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return True
    
class FrequentlyAskedQuestionsAdmin(CustomAdmin):
    list_display = ('question',)
    list_display_links= ('question',)
    search_fields = ('question',)

    
class SocialMediaUrlAdmin(admin.ModelAdmin):
    list_display = ('name','url')
    list_display_links= ('name','url')
    search_fields = ('name','url')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return True

class FilesAdmin(CustomAdmin):
    list_display = ('file_name','file')
    list_display_links= ('file_name','file')
    search_fields = ('file_name',)


    
admin.site.register(OurInitiatives, OurInitiativesAdmin)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(NewsLetter, NewsLetterAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(ContactHcg, ContactHcgAdmin)
admin.site.register(FrequentlyAskedQuestions, FrequentlyAskedQuestionsAdmin)
admin.site.register(SocialMediaURL, SocialMediaUrlAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Files, FilesAdmin)
admin.site.register(BulkEmail)