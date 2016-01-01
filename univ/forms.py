from django import forms


class InscriptionForm(forms.Form):
    nom = forms.CharField(label=" Nom  ",max_length=20)
    prenom = forms.CharField(max_length=20)
    date_naissance = forms.CharField(label="Date de naissance ")
