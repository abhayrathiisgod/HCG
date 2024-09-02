from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vacancies.views import JobTypeViewSet, JobOpeningViewSet, CandidateView, ProposalView, HasOpening

router = DefaultRouter()
router.register(r'job-types', JobTypeViewSet, basename='jobtype')
router.register(r'job-openings', JobOpeningViewSet, basename='jobopening')

urlpatterns = [
    path('', include(router.urls)),
    path('candidates/', CandidateView.as_view(), name='candidates'),
    path('proposals/', ProposalView.as_view(), name='proposals'),
    path('has-opening/', HasOpening.as_view(), name='has-opening'),
]
