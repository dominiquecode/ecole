from django import forms
from .models import Programme


class InscriptionForm(forms.Form):
    nom = forms.CharField(label=" Nom  ",max_length=20)
    prenom = forms.CharField(max_length=20)
    date_naissance = forms.DateField(label="Date de naissance ")
    courriel = forms.EmailField()
    date_inscription = forms.DateField(label="Date d'inscription ")


class ListeProgrammeForm(forms.Form):
    choix_programme = Programme.objects.all()
    liste_programme = forms.ModelMultipleChoiceField(choix_programme,
                                                     label="Liste des programmes",
                                                     widget=forms.RadioSelect)


