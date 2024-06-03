from rest_framework import serializers
from website.models import Designation, ContactUs, Files, Page , ContactHcg, NewsLetter, OurInitiatives,FrequentlyAskedQuestions, SocialMediaURL


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ('uuid','name','designation','image','Is_Board_Member','Is_Teams')


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('uuid','page_name','title','text')


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = ('email',)

class ContactHcgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactHcg
        fields = '__all__'

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('FullName', 'Email', 'PhoneNumber', 'Subject', 'Message')


class OurInitiativesPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurInitiatives
        exclude = ['id']

class FrequentlyAskedQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentlyAskedQuestions
        fields = ('uuid','question','answer')
        
class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaURL
        fields = ('uuid','name','url')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files 
        fields = ('uuid','file_name','file')

