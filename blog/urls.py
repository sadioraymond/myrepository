__author__ = 'Raymond'
from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',

    #url(r'^accueil$', 'home'),
    #url(r'^article/(?P<id_article>\d+)$', 'view_article'),
    #url(r'^article/(?P<id_article>\d+)$', 'view_article', name="afficher_article"),
    #url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', 'list_articles'),
    #url(r'^articlers/(?P<year>\d{4})/(?P<month>\d{2})$', 'list_articlers'),
    #url(r'^articler/(?P<id_article>\d+)$', 'view_articles'),
    url(r'^redirection$', 'view_redirection'),
    url(r'^redirections$', 'view_redirections'),
    url(r'^date$', 'date_actuelle'),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', 'addition'),
    url(r'^$', 'accueils'),
    url(r'^ajout$', 'ajout'),
    url(r'^modifier$', 'modif'),
    url(r'^modi/(?P<id>\d+)$', 'modifier'),
    url(r'^article$', 'lirer'),

)