# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('titre', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=6)),
            ],
            options={
                'verbose_name_plural': 'cours',
            },
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('date_naissance', models.DateField(null=True, blank=True)),
                ('code', models.CharField(max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date_inscripion', models.DateTimeField(auto_now_add=True)),
                ('cours', models.ForeignKey(to='univ.Cours')),
                ('etudiants', models.ForeignKey(to='univ.Etudiant')),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('date_naissance', models.DateField(null=True, blank=True)),
                ('code', models.CharField(max_length=6)),
                ('local', models.ForeignKey(to='univ.Local')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='etudiant',
            name='cours',
            field=models.ManyToManyField(to='univ.Cours', through='univ.Inscription'),
        ),
        migrations.AddField(
            model_name='cours',
            name='professeur',
            field=models.ForeignKey(to='univ.Professeur', null=True, blank=True),
        ),
    ]
