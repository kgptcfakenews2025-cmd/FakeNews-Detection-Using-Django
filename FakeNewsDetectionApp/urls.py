"""
URL configuration for FakeNewsDetection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from FakeNewsDetectionApp.views import Complaint, Feedback, LoginView, Reply, ViewUser

urlpatterns = [
    path('',LoginView.as_view(),name='Login'), 
    path('ViewUser',ViewUser.as_view(),name='ViewUser'), 
    path('Complaint',Complaint.as_view(),name='Complaint'), 
    path('Reply',Reply.as_view(),name='Reply'), 
    path('Feedback',Feedback.as_view(),name='Feedback'), 
    
    
]
