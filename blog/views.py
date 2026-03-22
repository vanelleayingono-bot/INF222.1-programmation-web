from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

from .models import Article
from .serializers import ArticleSerializer


# Création des views
class ArticleViewSet(viewsets.ModelViewSet):

    serializer_class = ArticleSerializer  

    def get_queryset(self):
        queryset = Article.objects.all()

        category = self.request.query_params.get('category')
        autor = self.request.query_params.get('autor')

        if category:
            queryset = queryset.filter(category__icontains=category)

        if autor:
            queryset = queryset.filter(autor__icontains=autor)

        return queryset


    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('query')

        if query:
            articles = Article.objects.filter(
                Q(title__icontains=query) |
                Q(contenu__icontains=query)
            )
        else:
            articles = Article.objects.all()

        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


def home(request):
    return render(request, 'page/home.html')