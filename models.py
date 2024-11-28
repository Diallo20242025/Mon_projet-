from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length = 50, blank = True)

    def __str__(self):
        return self.nom

class Tag(models.Model):
    nom = models.CharField(max_length = 50, blank = True)
    code_color = models.CharField(max_length=120)
    def __str__(self):
        return self.nom

# Create your models here.
class Article(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    titre = models.CharField(max_length = 50, blank = True)
    contenu = models.TextField(default= 200)
    date_pub = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photos/')
    tag = models.ManyToManyField(Tag)
    auteur = models.ForeignKey('Auteur', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.titre

class Auteur(models.Model):
    nom = models.CharField(max_length = 50, blank = True)
    telephone = models.IntegerField()
    adress = models.CharField(max_length = 100, blank = True)
    image = models.ImageField(upload_to='photos/')
    
    def __str__(self):
        return self.nom




class Commentaire(models.Model):
    Article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
    date_comment = models.DateTimeField(auto_now_add=True)
    date_accept = models.DateTimeField(auto_now_add=True)
    accept = models.BooleanField(default = True)



   

    