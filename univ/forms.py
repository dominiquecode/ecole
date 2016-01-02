from django import forms
from .models import Programme, Cours


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


class ListeCoursForm(forms.Form):
    choix_cours = Cours.objects.all()
    liste_cours = forms.ModelMultipleChoiceField(choix_cours,
                                                 label="Liste des cours",
                                                 widget=forms.CheckboxSelectMultiple)
