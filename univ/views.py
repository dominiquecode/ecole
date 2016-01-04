from django.shortcuts import render
from django.core.urlresolvers import reverse
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
    """
    Première étape du processus d'inscription d'un-e étudiant-e
    à une formation.
    Les données personnelles sont recuillies et le formulaire de choix
    de programme est affiché
    :param request:
    :return:
    """
    # vérification de la méthode et des champs de formulaire
    if request.method == "POST":
        formulaire_inscription = InscriptionForm(request.POST)
        if formulaire_inscription.is_valid():
            return HttpResponseRedirect(reverse("ins_prog_form"))

    else:
        formulaire_inscription = InscriptionForm(initial={"date_inscription": timezone.now(),
                                                          "courriel": "admin@tradom.ca"})

    # retourne les trois formulaires de la page
    return render(request, "ins_coordonnees_form.html",
                  {"formulaire_inscription": formulaire_inscription})


def inscription_programme_form(request):
    """
    Deuxième étape du processus d'inscription
    On récupére les choix de programme
    :param request:
    :return:
    """
    # vérification de la méthode et des champs de formulaire
    if request.method == "POST":
        formulaire_programme = ListeProgrammeForm(request.POST)
        if formulaire_programme.is_valid():
            return HttpResponseRedirect(reverse("ins_cours_form"))

    else:
        formulaire_programme = ListeProgrammeForm()

    # retourne les trois formulaires de la page
    return render(request, "ins_programmes_form.html",
                  {"formulaire_programme": formulaire_programme})


def inscription_cours_form(request):
    """
    Troisième étape du processus d'inscription
    on récupére les choix de cours
    :param request:
    :return:
    """
    # vérification de la méthode et des champs de formulaire
    if request.method == "POST":
        formulaire_cours = ListeCoursForm(request.POST)
        if formulaire_cours.is_valid():
            return HttpResponseRedirect(reverse("inscription_confirmation"))

    else:
        formulaire_cours = ListeCoursForm()

    # retourne les trois formulaires de la page
    return render(request,
                  "ins_cours_form.html",
                  {"formulaire_cours": formulaire_cours})


def inscription_confirmation(request):
    if request.method == "POST":
        print(request.__dict__)

    courriel = request.POST.get('courriel', '')
    date_inscription = request.POST.get("date_inscription", '')

    return render(request, "inscription_confirmation.html",
                  {"courriel": courriel,
                   "date_inscription": date_inscription})


def coordonnees(request):
    return render(request, "coordonnees.html", {})
