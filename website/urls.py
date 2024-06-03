from django.urls import path
from website.views import NewsletterView,PageView, DesignationView, FileView, ContactUsView, OurInitiativesPageView, SocialMediaView, ContactHcgView, FrequentlyAskedQuestionView

urlpatterns = [

    path('designation/', DesignationView.as_view({'get':'list'})),
    path('designation/<str:uuid>/', DesignationView.as_view({'get':'retrieve'})),

    path('newsletter/', NewsletterView.as_view({'post':'create'})),
    path('newsletter1234/', NewsletterView.as_view({'get':'list'})),
   
    path('contactus/', ContactUsView.as_view({'post':'create'})),

    path('page/',PageView.as_view({'get':'list'})),
    path('page/<str:uuid>',PageView.as_view({'get':'retrieve'})),
    
    path('our-initiatives/', OurInitiativesPageView.as_view({'get':'list'})),
    
    path('social-media/', SocialMediaView.as_view({'get':'list'})),
    path('social-media/<str:uuid>/', SocialMediaView.as_view({'get':'retrieve'})),
    
    
    path('contact-page/', ContactHcgView.as_view({'get':'list'})),
    
    path('frequently-asked-questions/', FrequentlyAskedQuestionView.as_view({'get':'list'})),
    path('frequently-asked-questions/<str:uuid>/', FrequentlyAskedQuestionView.as_view({'get':'retrieve'})),
   
    path('files/', FileView.as_view({'get':'list'})),
    path('files/<str:uuid>/', FileView.as_view({'get':'retrieve'})),
]
