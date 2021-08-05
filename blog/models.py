from django.db import models
from ckeditor.fields import RichTextField



class Categorie (models.Model):
    name = models.CharField(max_length=60, null=True)
    def __str__(self):
        return self.name

class Accueil(models.Model):
    title = models.CharField(max_length=200, null=True)
    resu = models.TextField(null=True)
    image=models.ImageField(upload_to="images/")
    body=RichTextField(null=True, blank=True)
    #body = models.TextField(null=True)
    date_creation=models.DateTimeField(auto_now_add=True)
    date_miseajour=models.DateTimeField(auto_now=True)
    categorie= models.ForeignKey(Categorie,max_length=60, null=True , on_delete=models.SET_NULL)
    def __str__(self):
        return self.title















