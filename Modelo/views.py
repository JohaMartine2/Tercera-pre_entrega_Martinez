from django.shortcuts import render
from .models import *

from .forms import *


def home(request):
    return render(request, "Modelo/index.html")

def industries(request):
    contexto = {"Industries": Industries.objects.all()}
    return render(request, "Modelo/Industries.html", contexto)

def services(request):
    contexto = {"Services": Services.objects.all()}
    return render(request, "Modelo/Services.html", contexto)

def team(request):
    contexto = {"Team": Team.objects.all()}
    return render(request, "Modelo/Team.html", contexto)


#Formularios

def feedbackForm(request):
    if request.method == "POST":
        miForm = FeedbackForm(request.POST)
        if miForm.is_valid():
            feedback_name = miForm.cleaned_data.get("name")
            feedback_email = miForm.cleaned_data.get("email")
            feedback_phone = miForm.cleaned_data.get("phone")
            feedback_message = miForm.cleaned_data.get("message")
            feedback = Feedback(name = feedback_name, email = feedback_email, phone = feedback_phone, message= feedback_message)
            feedback.save()
            contexto = {"Feedbacks": Feedback.objects.all() }
            return render(request, "Modelo/feedbackForm.html")
    else:
        miForm = FeedbackForm()

    return render(request, "Modelo/feedbackForm.html", {"form": miForm})


def teamForm(request):
    if request.method == "POST":
        miForm = TeamForm(request.POST)
        if miForm.is_valid():
            teamfull_name = miForm.cleaned_data.get("full_name")
            team_email = miForm.cleaned_data.get("email")
            team_phone = miForm.cleaned_data.get("phone")
            team_department = miForm.cleaned_data.get("department")
            team_bio = miForm.cleaned_data.get("bio")
            team = Team(full_name = teamfull_name, email = team_email, phone = team_phone, department= team_department, bio = team_bio)
            team.save()
            contexto = {"Feedbacks": Team.objects.all() }
            return render(request, "Modelo/TeamForm.html", contexto)
    else:
        miForm = TeamForm()

    return render(request, "Modelo/teamForm.html", {"form": miForm})