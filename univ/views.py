from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Programme, Professeur, Cours
from .forms import InscriptionForm, ListeProgrammeForm, ListeCoursForm
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
    les_programmes = Programme.objects.all()
    professeurs = Professeur.objects.all()
    cours = Cours.objects.all()

    return render(request, "organisation.html",
                  {"programmes": les_programmes,
                   "professeurs": professeurs,
                   "cours": cours, }
                  )


def inscription_form(request):
    # vérification de la méthode et des champs de formulaire
    if request.method == "POST":
        formulaire_inscription = InscriptionForm(request.POST)
        formulaire_programme = ListeProgrammeForm(request.POST)
        formulaire_cours = ListeProgrammeForm(request.POST)
        if formulaire_inscription.is_valid() and formulaire_programme.is_valid() and formulaire_cours.is_valid():
            return HttpResponseRedirect("/inscriptions_form/")

    else:
        formulaire_inscription = InscriptionForm(initial={"date_inscription": timezone.now()})
        formulaire_programme = ListeProgrammeForm()
        formulaire_cours = ListeCoursForm()

    # retourne les trois formulaires de la page
    return render(request,
                  "inscription_form.html",
                  {"formulaire_inscription": formulaire_inscription,
                   "formulaire_programme": formulaire_programme,
                   "formulaire_cours": formulaire_cours})


def inscription_confirmation(request):
    return render(request, "inscription_confirmation.html", {})


def coordonnees(request):
    return render(request, "coordonnees.html", {})
