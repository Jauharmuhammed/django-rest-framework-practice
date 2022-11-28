from rest_framework import viewsets, generics
from .models import Article
from .serializers import ArticleSerializer


#% generic viewset based views
class ArticleGenericViewset(viewsets.GenericViewSet,generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

