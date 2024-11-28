from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name= 'index'),
    path('deshbord/', deshbord , name='deshbord'),
    path('articleDetail/<int:article_id>', articleDetail, name='articleDetail'),
    path('liste_article/', liste_article, name = 'liste_article'),
    path('liste_auteur/', liste_auteur, name = 'liste_auteur'),
    path('liste_categorie/', liste_categorie, name = 'liste_categorie'),
    path('liste_tag/', liste_tag, name = 'liste_tag'),
    path('ajouter_article/', ajouter_article, name= 'ajouter_article'),
    path('update/<int:article_id>/', update, name= 'update'),
    path('delete/<int:article_id>/', delete, name= 'delete'),
    path('ajouter_auteur/', ajouter_auteur, name= 'ajouter_auteur'),
    path('update_auteur/<int:auteur_id>/', update_auteur, name= 'update_auteur'),
    path('auteur_delete/<int:auteur_id>/',auteur_delete, name= 'auteur_delete'),
    path('create_category/', create_category, name= 'create_category'),
    path('update_categorie/<int:categorie_id>/', update_categorie, name= 'update_categorie'),
    path('categorie_delete/<int:categorie_id>/',categorie_delete, name= 'categorie_delete'),
    path('add_tag/', add_tag, name= 'add_tag'),
    path('update_tag/<int:tag_id>/', update_tag, name= 'update_tag'),
    path('tag_delete/<int:tag_id>/',tag_delete, name= 'tag_delete'),
    
    
]