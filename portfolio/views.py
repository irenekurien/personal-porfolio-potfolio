from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()  # Class name dot object dot all
    return render(request, 'Portfolio/home.html', {'projects': projects})
