from django.test import TestCase


# Create your tests here.
class UrlVerification(TestCase):

    def test_univ(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_programmes(self):
        response = self.client.get("/programmes")
        self.assertEquals(response.status_code, 200)

    def test_programme_organisation(self):
        response = self.client.get("/programmes/organisation")
        self.assertEquals(response.status_code, 200)

    def test_inscription(self):
        response = self.client.get("/inscriptions")
        self.assertEquals(response.status_code, 200)

    def test_inscription_formulaire(self):
        response = self.client.get("/inscriptions/formulaire")
        self.assertEquals(response.status_code, 200)

    def test_inscription_confirmation(self):
        response = self.client.get("/inscriptions/confirmation")
        self.assertEquals(response.status_code, 200)

    def test_endev(self):
        response = self.client.get("/endev")
        self.assertEquals(response.status_code, 200)

    def test_vie_courante(self):
        response = self.client.get("/vie_courante")
        self.assertEquals(response.status_code, 200)

