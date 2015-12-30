from django.contrib import admin
from univ.models import Professeur, Etudiant, Local, Inscription, Cours

# Register your models here.
admin.site.register(Professeur)
admin.site.register(Etudiant)
admin.site.register(Local)
admin.site.register(Inscription)
admin.site.register(Cours)
