from django.contrib import admin
from .models import Article 
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre','contenu','auteur','date','categorie','tags')

admin.site.register(Article,ArticleAdmin)
