
from django.urls import path

from FakeNewsDetectionApp.views import *

urlpatterns = [
    path('',LoginView.as_view(),name='Login'), 
    path('ViewUser',ViewUser.as_view(),name='ViewUser'), 
    path('AcceptUser/<int:id>',AcceptUser.as_view(),name='AcceptUser'),
    path('RejectUser/<int:id>',RejectUser.as_view(),name='RejectUser'),
    path('Complaint',Complaint.as_view(),name='Complaint'), 
    path('Reply',Reply.as_view(),name='Reply'), 
    path('Feedback',Feedback.as_view(),name='Feedback'), 
    path('adminhome',AdminHome.as_view(),name='Adminhome'), 
    
    
]
