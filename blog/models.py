from django.db import models

# Create your models here

class Article(models.Model):
    titre = models.CharField(max_length = 50)
    contenu = models.CharField(max_length=50)
    auteur = models.CharField(max_length = 255)
    date =models.DateField(auto_now_add = True )
    categorie = models.TextField()
    tags = models.CharField(max_length = 25)

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.titre