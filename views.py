from django.shortcuts import render, redirect
from .models import Categorie, Article, Auteur, Tag, Commentaire
from .forms import ArticleForm, AuteurForm, CategorieForm, TagForm



# Create your views here.
def index(request): 
    articles= Article.objects.all()
    categories=Categorie.objects.all()

    context= { 
        'categories': categories,
        'articles': articles,
    }
    
    return render(request, 'blog/front_office/index.html', context)

def deshbord(request):
    return render(request, 'blog/back_office/deshbord.html')

def articleDetail(request, article_id):
    article = Article.objects.get(id = article_id)
    context = { 'article': article}
    return render(request,'blog/front_office/articleDetail.html', context)

def liste_article(request):
    articles= Article.objects.all()
    context = { 'articles': articles}
    return render(request, 'blog/back_office/liste_article.html', context)

# =================Article par categorie========================



def liste_auteur(request):
    auteurs = Auteur.objects.all()
    context = { 'auteur': auteurs}
    return render(request, 'blog/back_office/liste_auteur.html', context)

def liste_categorie(request):
    categories = Categorie.objects.all()
    context = {'categorie': categories }
    return render(request, 'blog/back_office/liste_categorie.html', context)

def liste_tag(request):
    tag = Tag.objects.all()
    context = {'tag': tag}
    return render(request, 'blog/back_office/liste_tag.html', context)


 # ============================crée, ajouter, mise à jour et supprimer une categorie=====================


def ajouter_article(request):
    form = ArticleForm() 
    if request.method == 'POST':
        form = ArticleForm(request.POST , request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('liste_article')

    context = {
        "form": form
    }

    return render(request, 'blog/back_office/ajouter_article.html', context)

def update(request, article_id):
    article = Article.objects.get(id = article_id)

    form = ArticleForm(instance=article)
    if request.method== "POST":
        form = ArticleForm(instance=article, data = request.POST, files= request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_article')
    context = {'form': form}
    return render(request,'blog/back_office/update.html', context)

def delete(request, article_id):
    article = Article.objects.get(id =article_id)
    article.delete()
    return redirect('liste_article')


 # ============================crée, ajouter, mise à jour et supprimer une auteur =====================

def ajouter_auteur(request):
    form = AuteurForm()
    if request.method == "POST":
        form = AuteurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_auteur')
    context ={ 'form': form}
    return render(request, 'blog/back_office/ajouter_auteur.html', context)


def update_auteur(request, auteur_id):
    auteur = Auteur.objects.get(id = auteur_id)
    form = AuteurForm(instance=auteur)
    if request.method== "POST":
        form = AuteurForm(instance = auteur, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_auteur')
    context = {'form': form}
    return render(request,'blog/back_office/update_auteur.html', context)


def auteur_delete(request, auteur_id):
    auteur = Auteur.objects.get(id =auteur_id)
    auteur.delete()
    return redirect('liste_auteur')
 
 # ============================crée, ajouter, mise à jour et supprimer une categorie=====================


def create_category(request):
    form = CategorieForm()
    if request.method == "POST":
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_categorie')
    context ={'form': form}
    return render(request, 'blog/back_office/create_category.html', context)


def update_categorie(request, categorie_id):
    categories = Categorie.objects.get(id = categorie_id)
    form = CategorieForm(instance=categorie)
    if request.method== "POST":
        form = CategorieForm(instance=categorie, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_categorie')
    context = {'form': form}
    return render(request,'blog/back_office/update_categorie.html', context)

def categorie_delete(request, categoriee_id):
    categorie = Categorie.objects.get(id =categorie_id)
    categorie.delete()
    return redirect('liste_categorie')


 # ============================crée, ajouter, mise à jour et supprimer une tag =====================

def add_tag(request):
    form = TagForm()
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_tag')
    context ={'form': form}
    return render(request, 'blog/back_office/add_tag.html', context)


def update_tag(request, tag_id):
    tag = Tag.objects.get(id = tag_id)
    form = TagForm(instance = tag)
    if request.method== "POST":
        form = TagForm(instance= tag, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_tag')
    context = {'form': form}
    return render(request,'blog/back_office/update_tag.html', context)

def tag_delete(request, tag_id):
    tag =Tag.objects.get(id = tag_id)
    tag.delete()
    return redirect('liste_tag')


   

    



