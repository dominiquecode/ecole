from django.shortcuts import render
from .models import Programme,Professeur,Cours


# Create your views here.
def acceuil(request):
    return render(request, "accueil.html", {})


def inscription(request):
    return render(request, "inscriptions.html", {})


def programmes(request):
    return render(request, "programmes.html", {})


def endev(request):
    return render(request, "endev.html", {})


def vie_courante(request):
    return render(request, "vie_courante.html", {})


def organisation(request):
    programmes = Programme.objects.all()
    professeurs = Professeur.objects.all()
    cours = Cours.objects.all()
    context = {
        "programmes": programmes,
        "professeurs": professeurs,
        "cours": cours,
    }
    return render(request, "organisation.html", context)