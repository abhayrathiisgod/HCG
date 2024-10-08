from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from vacancies.serializers import JobTypeSerializer, ProposalSerializer, JobOpeningSerializer, JobOpeningDetailSerializer, CandidateSerializer, HasOpeningSerializer
from vacancies.models import JobType, JobOpening, Candidate, Proposal

class JobTypeViewSet(ReadOnlyModelViewSet):
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer
    lookup_field = 'uuid'

class JobOpeningViewSet(ReadOnlyModelViewSet):
    queryset = JobOpening.objects.all()
    serializer_class = JobOpeningSerializer
    lookup_field = 'uuid'

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
    def retrieve(self, request, uuid=None):
        queryset = self.get_queryset()
        job_opening = get_object_or_404(queryset, uuid=uuid)
        serializer = JobOpeningDetailSerializer(job_opening)
        return Response(serializer.data)

class CandidateView(generics.CreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class HasOpening(APIView):
    def get(self, request, *args, **kwargs):
        has_opening = 'True' if JobOpening.objects.filter(is_published=True).count() > 0 else 'False'
        data = {'has_opening': has_opening}
        serializer = HasOpeningSerializer(data)
        return Response(serializer.data)

class ProposalView(generics.CreateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
