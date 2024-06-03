import django_filters
from .models import Files, Page, Designation

class FilesFilter(django_filters.FilterSet):
    file_name = django_filters.ChoiceFilter(choices=Files.file_type)

    class Meta:
        model = Files
        fields = ['file_name']

class PageFilter(django_filters.FilterSet):
    page_name = django_filters.ChoiceFilter(choices=Page.page_type)

    class Meta:
        model = Page
        fields = ['page_name']

class DesignationFilter(django_filters.FilterSet):
    Is_Board_Member = django_filters.BooleanFilter(label='Is Board Member')
    Is_Teams = django_filters.BooleanFilter(label='Is Teams')

    class Meta:
        model = Designation
        fields = ['Is_Board_Member', 'Is_Teams']