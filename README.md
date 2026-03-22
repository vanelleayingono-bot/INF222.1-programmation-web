INF222.1 - Programmation Web

Dépôt du TP de 222.1

README - Projet Blog API Django

### DESCRIPTION DU PROJET
Ce projet est une API de blog développée avec Django et Django REST Framework.
Il permet de gérer des articles avec plusieurs fonctionnalités essentielles : création, consultation, filtrage et recherche.
L’objectif principal est de mettre en place une API simple et fonctionnelle pour manipuler des données de type blog.

### TECHNOLOGIES UTILISÉES

Python
Django
Django REST Framework
SQLite (base de données par défaut)

III.###### STRUCTURE DU PROJET
Le projet est organisé autour de deux parties principales :

Projet principal : configuration globale
Application blog : logique métier
Modèles : gestion des données
Vues et endpoints : API
Admin : gestion via interface Django
Templates HTML : pages simples

### MODÈLE DE DONNÉES

class Article(models.Model):
    titre = models.CharField(max_length=50)
    contenu = models.CharField(max_length=50)
    auteur = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    categorie = models.TextField()
    tags = models.CharField(max_length=25)

Ce modèle représente un article de blog avec ses informations principales.
Les articles sont triés du plus récent au plus ancien.
Exemple explicatif : un article pourrait avoir pour auteur “Sandy” pour illustrer le filtrage par auteur.

### INTERFACE D’ADMINISTRATION

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre','auteur','date','categorie')

admin.site.register(Article, ArticleAdmin)

Permet de gérer les articles directement depuis l’interface d’administration Django.
Exemple : on peut voir tous les articles écrits par “Sandy” dans l’admin.

### CONFIGURATION DU PROJET
Dans settings.py, l’application blog et Django REST Framework sont activés pour exposer les endpoints de l’API :

INSTALLED_APPS = [
    'blog',
    'rest_framework',
]

La base de données SQLite est utilisée par défaut et un répertoire templates est configuré pour les pages HTML.

VII. VUES ET ENDPOINTS DE L’API

CRUD

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

Endpoints principaux :

GET /api/articles/ : liste tous les articles
POST /api/articles/ : créer un article
GET /api/articles/{id}/ : récupérer un article spécifique
PUT /api/articles/{id}/ : mettre à jour un article
DELETE /api/articles/{id}/ : supprimer un article

Filtrage

def get_queryset(self):
    queryset = Article.objects.all()
    category = self.request.query_params.get('category')
    autor = self.request.query_params.get('autor')
    if category:
        queryset = queryset.filter(categorie__icontains=category)
    if autor:
        queryset = queryset.filter(auteur__icontains=autor)
    return queryset

Exemples d’utilisation :

/api/articles/?category=tech
/api/articles/?autor=Sandy (exemple illustratif)

Recherche

@action(detail=False, methods=['get'])
def search(self, request):
    query = request.query_params.get('query')
    if query:
        articles = Article.objects.filter(
            Q(titre__icontains=query) |
            Q(contenu__icontains=query)
        )

Endpoint : /api/articles/search/?query=django

### INTERFACE UTILISATEUR

def home(request):
    return render(request, 'page/home.html')

Page d’accueil simple.
Exemple de message affiché : “Bienvenue Sandy” pour illustrer l’affichage personnalisé d’un utilisateur.

### CONFIGURATION ET LANCEMENT

pip install django djangorestframework
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Ces commandes permettent d’installer les dépendances, configurer la base de données et lancer le serveur.

### UTILISATION DES ENDPOINTS
Les endpoints permettent :

d’accéder à la liste des articles
de filtrer les résultats par catégorie ou auteur
d’effectuer des recherches par titre ou contenu

Exemples :

/api/articles/
/api/articles/?category=tech
/api/articles/?autor=Sandy (exemple illustratif)
/api/articles/search/?query=django

### REMARQUES

Correction d’incohérences entre noms de champs (anglais/français)
Correction des filtres et de la logique de recherche

### AMÉLIORATIONS POSSIBLES

Authentification pour sécuriser les endpoints
Gestion des utilisateurs
Ajout d’images aux articles
Pagination des résultats
Système de commentaires et likes
