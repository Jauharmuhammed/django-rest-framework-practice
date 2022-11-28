from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer

#% model viewset based views
class ArticleModelViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

#^ This last Three lines of code can replace a lot of normal used functionality that we gain here.