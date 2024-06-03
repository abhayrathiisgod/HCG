from website.models import Designation, NewsLetter,Page, ContactUs,Files, OurInitiatives, ContactHcg, FrequentlyAskedQuestions, SocialMediaURL
from website.serializers import DesignationSerializer, NewsletterSerializer, PageSerializer,FileSerializer, ContactHcgSerializer,ContactUsSerializer,SocialMediaSerializer, FrequentlyAskedQuestionSerializer, OurInitiativesPageSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .filters import FilesFilter, PageFilter, DesignationFilter


class DesignationView(ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DesignationFilter
    lookup_field = 'uuid'


class PageView(ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PageFilter

class NewsletterView(ModelViewSet):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsletterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {'message': 'Congratulations You have successfully subscribed !!'},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

class ContactUsView(ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {'message': 'Contact request submitted successfully!'},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

class OurInitiativesPageView(ModelViewSet):
    queryset = OurInitiatives.objects.all()
    serializer_class = OurInitiativesPageSerializer

class ContactHcgView(ModelViewSet):
    queryset = ContactHcg.objects.all()
    serializer_class = ContactHcgSerializer

class FrequentlyAskedQuestionView(ModelViewSet):
    queryset = FrequentlyAskedQuestions.objects.all()
    serializer_class = FrequentlyAskedQuestionSerializer
    pagination_class = None 
    lookup_field = 'uuid'

class SocialMediaView(ModelViewSet):
    queryset = SocialMediaURL.objects.all()
    serializer_class = SocialMediaSerializer

class FileView(ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FilesFilter
    lookup_field = 'uuid'
