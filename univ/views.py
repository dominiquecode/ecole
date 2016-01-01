from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Programme, Professeur, Cours
from .forms import InscriptionForm
from django.utils import timezone

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


def inscription_form(request):
    # vérification de la méthode et des champs de formulaire
    if request.method == "POST":
        formulaire = InscriptionForm(request.POST)
        if formulaire.is_valid():
            formulaire.date_inscription = timezone.now()
            return HttpResponseRedirect("/inscriptions_form/")
    else:
        formulaire = InscriptionForm()

    return render(request, "inscription_form.html", {"formulaire": formulaire})
