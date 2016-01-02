from django.test import TestCase
from univ.models import Etudiant, Professeur, Local

class EtudiantTestCase(TestCase):

    def setUp(self):
        Etudiant.objects.create(nom="test1", prenom="prenomtest1")
        Etudiant.objects.create(nom="test2", prenom="prenomtest2")

    def test_creation_etudiant(self):
        etu1 = Etudiant.objects.get(pk=1)
        etu2 = Etudiant.objects.get(pk=2)

        self.assertEquals(etu1.nom, "test1")
        self.assertEquals(etu2.nom, "test2")

    def test_modification_nom_etudiant(self):
        etu1 = Etudiant.objects.get(pk=1)
        self.assertEquals(etu1.nom, "test1")
        etu1.nom = "testmodifié"
        self.assertEquals(etu1.nom, "testmodifié")

    def test_modification_pk(self):
        etu1 = Etudiant.objects.get(pk=1)
        etu1.pk = 2
        etu1.save()
        etu2 = Etudiant.objects.get(pk=2)
        self.assertEquals(etu2.nom, "test1")
        self.assertEquals(etu1.nom, "test1")


class ProfesseurTestCase(TestCase):

    def setUp(self):
        local = Local.objects.create(nom="a100")
        Professeur.objects.create(nom="prof1", prenom="profe1prenom", local=local)
        Professeur.objects.create(nom="prof2", prenom="profe2prenom", local=local)

    def test_creation_professeur(self):
        prof1 = Professeur.objects.get(pk=1)
        prof2 = Professeur.objects.get(pk=2)

        self.assertEquals(prof1.nom, "prof1")
        self.assertEquals(prof2.nom, "prof2")
        self.assertEquals(prof1.local.nom, "a100")
        self.assertEquals(prof2.local.nom, "a100")

    def test_modification_pk_professeur(self):
        prof1 = Professeur.objects.get(pk=1)
        self.assertEquals(prof1.nom, "prof1")
        prof1.pk = 2
        prof1.save()
        prof2 = Professeur.objects.get(pk=2)
        self.assertEquals(prof1.nom, prof2.nom)

    def test_modification_nom_professeur(self):
        prof1 = Professeur.objects.get(pk=1)
        self.assertEquals(prof1.nom, "prof1")
        prof1.nom = "test"
        prof1.save()
        self.assertEquals(prof1.nom, "test")
