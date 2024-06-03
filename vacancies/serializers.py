from rest_framework import serializers
from vacancies.models import JobType, JobOpening, Candidate, Proposal

class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ('uuid','JobTypeName',)

class JobOpeningSerializer(serializers.ModelSerializer):
    JobType = JobTypeSerializer()
    class Meta:
        model = JobOpening
        fields = ('id','PositionName', 'JobType', 'Deadline')

class JobOpeningDetailSerializer(serializers.ModelSerializer):
    JobType = JobTypeSerializer()
    class Meta:
        model = JobOpening
        fields = ('PositionName', 'JobType', 'OpeningDate', 'Deadline', 'AboutTheRole', 'JobRequirements')


class CandidateSerializer(serializers.ModelSerializer):
    Position = JobOpening()
    class Meta:
        model = Candidate
        fields = ('FirstName', 'LastName', 'Email', 'PhoneNumber', 'Position', 'CV')


class HasOpeningSerializer(serializers.Serializer):
    has_opening = serializers.BooleanField()

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ('FirstName', 'LastName', 'Email', 'PhoneNumber', 'ProjectName', 'ProjectFile')
