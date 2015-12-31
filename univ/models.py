from django.db import models


# Create your models here.
class Personne(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    date_naissance = models.DateField(null=True, blank=True)

    class Meta:
        abstract=True

    def __str__(self):
        return self.nom


class Local(models.Model):
    nom = models.CharField(max_length=10)

    def __str__(self):
        return self.nom


class Programme(models.Model):
    nom = models.CharField(max_length=30)
    code = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)


    def _get_identifiant(self):
        return "%s (%s)" % (self.nom, self.code)
    identifiant = property(_get_identifiant)

    def _get_liste_cours(self):
        return self.cours_set.all()
    liste_cours = property(_get_liste_cours)

    def __str__(self):
        return self.nom


class Professeur(Personne):
    code = models.CharField(max_length=6)
    local = models.ForeignKey(Local)

    def _get_identifiant(self):
        return "%s %s (%s)" % (self.nom, self.prenom, self.code)
    identifiant = property(_get_identifiant)

    def _get_liste_cours(self):
        return self.cours_set.all()
    liste_cours = property(_get_liste_cours)

    def __str__(self):
        return "%s %s" % (self.nom, self.prenom)


class Cours(models.Model):
    titre = models.CharField(max_length=20)
    code = models.CharField(max_length=6)
    professeur = models.ForeignKey(Professeur, null=True, blank=True)
    programme = models.ForeignKey(Programme, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'cours'

    def _get_liste_etudiant(self):
        return self.etudiant_set.all()
    liste_etudiants = property(_get_liste_etudiant)

    def __str__(self):
        return self.titre


class Etudiant(Personne):
    code = models.CharField(max_length=5)
    cours = models.ManyToManyField(Cours, through='Inscription')

    def _get_identifiant(self):
        return '%s %s (%s)' % (self.nom, self.prenom, self.code)
    identifiant = property(_get_identifiant)

    def _get_liste_cours(self):
        return self.cours.all()
    liste_cours = property(_get_liste_cours)


class Inscription(models.Model):
    cours = models.ForeignKey(Cours)
    etudiants = models.ForeignKey(Etudiant)
    date_inscripion = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.date_inscripion)
