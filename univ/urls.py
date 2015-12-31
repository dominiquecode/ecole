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
    url(r'^programmes', views.programmes, name="programmes"),
    url(r'^inscriptions', views.inscription, name="inscriptions"),
    url(r'^endev', views.endev, name="endev"),
    url(r'^vie_courante', views.vie_courante, name="vie_courante"),
]
