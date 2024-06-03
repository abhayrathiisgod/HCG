from django.contrib import admin
from vacancies.models import JobType, JobOpening, Candidate, Proposal
from website.admin import CustomAdmin

# Register your models here.

class JobTypeAdmin(CustomAdmin):
    actions = None
    list_display = ('JobTypeName',) 
    list_display_links = ('JobTypeName',)

class JobOpeningAdmin(CustomAdmin):
    list_display = ('PositionName','JobType','OpeningDate','Deadline','is_published')
    list_display_links = ('PositionName','JobType','OpeningDate','Deadline','is_published')
    search_fields = ('PositionName',)
    list_filter = ('JobType','is_published')
    readonly_fields = ('Created_at','Updated_at',)

class CandidateAdmin(CustomAdmin):
    list_display = ('Position','LastName','Email','PhoneNumber')
    list_display_links = ('Position','LastName','Email','PhoneNumber')
    search_fields = ('FirstName','LastName')
    list_filter = ('Position', 'Created_at')

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None) -> bool:
        return False
    
class ProposalAdmin(CustomAdmin):
    list_display = ('ProjectName','FirstName','LastName','Email')
    list_display_links = ('ProjectName','FirstName','LastName','Email')
    search_fields = ('ProjectName',)
    list_filter = ('Created_at','Updated_at')


    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None) -> bool:
        return False

admin.site.register(JobType , JobTypeAdmin)
admin.site.register(JobOpening, JobOpeningAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Proposal,ProposalAdmin)
