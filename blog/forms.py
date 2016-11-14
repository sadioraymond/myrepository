__author__ = 'Raymond'
from django import forms
from blog.models import Article, Categorie
from django.db import models
#from django.forms import ModelForm

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('titre','auteur','categorie','contenu')

class ArticleForms(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('auteur','titre','contenu')


