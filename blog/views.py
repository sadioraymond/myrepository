from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from blog.models import Categorie, Article
from blog.forms import ArticleForm, ArticleForms
from django.views import generic
from django.views.generic.edit import FormMixin
from django.utils import timezone
# Create your views here.

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)

def acceuil(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Diaye Prek !</p>"""
    return HttpResponse(text)

def view_article(request, id_article):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """

    text = "Vous avez demandé l'article #{0} !".format(id_article)
    return HttpResponse(text)

def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """

    text = "Vous avez demandé les articles de {0} {1}.".format(month, year)
    return HttpResponse(text)

def view_articles(request, id_article):
    # Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
    if int(id_article) > 100:
        raise Http404

    return redirect(view_redirections)

def list_articlers(request, year, month):
    # Il veut des articles ? Soyons fourbe et redirigeons le vers djangoproject.com
    return redirect(view_redirections)

def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")

def view_redirections(request):
    #return redirect('blog.views.view_article', id_article=42)
    return redirect('afficher_article', id_article=42)


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())

def accueils(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

def lires(request, id):
    """ Afficher un article complet """
    pass # Le code de cette fonction est donné un peu plus loin.

def lirer(request):
    try:
        article = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'blog/lire.html', {'articles': article})

def lire(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire.html', {'articles':article})

def ajout(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        #prepopulated_fields = {'Article.slug': ('Article.titre', ), }
        if form.is_valid():
            form.save()
            return redirect(view_redirection)
    else:
        form = ArticleForm
    return render(request, 'blog/ajout.html', locals())

def modifi(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/modif.html', {'articles':article})


def modifier(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleForms(request.POST, instance=article)
        if form.is_valid():
            form.save()

    else:
        form = ArticleForms(instance=article)
    return render(request, 'blog/modif.html', locals())

def modif(request):
    try:
        article = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'blog/modifier.html', {'articles': article})