from django import forms


class InscriptionForm(forms.Form):
    nom = forms.CharField(label=" Nom  ",max_length=20)
    prenom = forms.CharField(max_length=20)
    date_naissance = forms.DateField(label="Date de naissance ")
    courriel = forms.EmailField()
    date_inscription = forms.DateField(label="Date d'inscription ")

