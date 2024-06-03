from django.urls import path
from vacancies.views import JobTypeViewSet,ProposalView, JobOpeningViewSet, CandidateView, HasOpening

urlpatterns = [
    path('jobtypes/', JobTypeViewSet.as_view({'get':'list'}), name='jobtypes'),
    path('jobtypes/<str:uuid>/', JobTypeViewSet.as_view({'get':'retrieve'}), name='jobtype-detail'),
    path('jobopenings/', JobOpeningViewSet.as_view({'get':'list'}), name='jobopenings'),
    path('jobopenings/<str:uuid>/', JobOpeningViewSet.as_view({'get':'retrieve'}), name='jobopening-detail'),
    path('candidates/', CandidateView.as_view(), name='candidates'),
    path('proposals/', ProposalView.as_view(), name='proposals'),
    path('has_opening/', HasOpening.as_view()),
]