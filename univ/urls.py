"""Ecole URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from univ import views

urlpatterns = [
    url(r'^$', views.acceuil, name='accueil'),
    url(r'^programmes$', views.programmes, name="programmes"),
    url(r'^programmes/organisation$', views.organisation, name="organisation"),
    url(r'^inscriptions$', views.inscription, name="inscriptions"),
    url(r'^inscriptions/formulaire$', views.inscription_form, name="inscription_form"),
    url(r'^inscriptions/formulaires/programme$', views.inscription_programme_form, name="ins_prog_form"),
    url(r'^inscriptions/formulaires/cours$', views.inscription_cours_form, name="ins_cours_form"),
    url(r'^inscriptions/confirmation$', views.inscription_confirmation, name="inscription_confirmation"),
    url(r'^endev$', views.endev, name="endev"),
    url(r'^vie_courante$', views.vie_courante, name="vie_courante"),
    url(r'^coordonnees$', views.coordonnees, name="coordonnees"),

]
