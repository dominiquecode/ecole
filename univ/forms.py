from django import forms
from django.forms import ModelForm
from .models import Programme, Cours, Etudiant


class EtudiantForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = ["nom", "prenom", "code", "cours"]


class InscriptionForm(forms.Form):
    """
    Le formulaire d'inscription d'un-e étudiant-e
    généré sans partir du model correspondant
    c'est la première version.
    """
    nom = forms.CharField(label=" Nom  ",max_length=20)
    prenom = forms.CharField(max_length=20, label="Prénom ")
    date_naissance = forms.DateField(label="Date de naissance ")
    courriel = forms.EmailField(label="Courriel ")
    date_inscription = forms.DateField(label="Date d'inscription ")



class ListeProgrammeForm(forms.Form):
    """
    le formulaire redonne la liste des programmes actifs dans l'application
    un seul champ utilisé dans le template pour obtenir une liste ouverte
    en mode bouton radio (choix exclusif)
    """
    choix_programme = Programme.objects.all()
    liste_programme = forms.ModelMultipleChoiceField(choix_programme,
                                                     label="Liste des programmes",
                                                     widget=forms.RadioSelect)


class ListeCoursForm(forms.Form):
    """
    le formulaire redonne la liste des cours actifs dans l'application
    Un seul champ utilisé dans le template pour obtenir une liste
    de case à cocher (choix multiple)
    """
    choix_cours = Cours.objects.all()
    liste_cours = forms.ModelMultipleChoiceField(choix_cours,
                                                 label="Liste des cours",
                                                 widget=forms.CheckboxSelectMultiple)


class InscriptionProcess(forms.Form):
    nom = forms.CharField(label=" Nom  ",max_length=20)
    prenom = forms.CharField(max_length=20, label="Prénom ")
    date_naissance = forms.DateField(label="Date de naissance ")
    courriel = forms.EmailField(label="Courriel ")
    date_inscription = forms.DateField(label="Date d'inscription ")
    choix_programme = Programme.objects.all()
    liste_programme = forms.ModelMultipleChoiceField(choix_programme,
                                                     label="Liste des programmes",
                                                     widget=forms.RadioSelect)
