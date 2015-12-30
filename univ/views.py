from django.shortcuts import render


# Create your views here.
def acceuil(request):
    return render(request, "accueil.html", {})


def inscription(request):
    return render(request, "inscriptions.html", {})


def programmes(request):
    return render(request, "programmes.html", {})


def endev(request):
    return render(request, "endev.html", {})