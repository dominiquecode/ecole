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
    # vérification de la méthode et des champs de formulairej
    if request.method == "POST":
        formulaire_inscription = InscriptionForm(request.POST)
        formulaire_programme = ListeProgrammeForm(request.POST)
        formulaire_cours = ListeProgrammeForm(request.POST)
        if formulaire_inscription.is_valid() and formulaire_programme.is_valid() and formulaire_cours.is_valid():
            return HttpResponseRedirect("/inscriptions_form/")

    else:
        formulaire_inscription = InscriptionForm(initial={"date_inscription": timezone.now()})
        formulaire_programme = ListeProgrammeForm()
        formulaire_cours =ListeCoursForm()

    return render(request,
                  "inscription_form.html",
                  {"formulaire_inscription": formulaire_inscription,
                   "formulaire_programme":formulaire_programme,
                   "formulaire_cours": formulaire_cours}
                )


def inscription_confirmation(request):
    nom = request.POST["nom"]
    prenom = request.POST["prenom"]

    context = {"nom": nom, "prenom": prenom}
    return render(request, "inscription_confirmation.html", context)


def coordonnees(request):
    courriel = request.POST["adresse_courriel"]
    mdp = request.POST["mot_de_passe"]

    context = {"courriel": courriel, "mdp": mdp}
    return render(request, "coordonnees.html", context)