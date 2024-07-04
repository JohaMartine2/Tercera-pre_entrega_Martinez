from django.urls import path, include
from Modelo.views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('Industries/', industries, name = 'Industries'),
    path('Services/', services, name = 'Services'),
    path('Team/', team, name = 'Team'),
    

    path('FeedbackForm/', feedbackForm, name = 'FeedbackForm'),
    path('TeamForm/', teamForm, name = 'TeamForm')
]