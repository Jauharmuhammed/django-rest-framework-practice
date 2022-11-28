from rest_framework import generics, mixins
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#% generic views
class ArticleGenericView(generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request):
        query_set = self.get_queryset()
        serializer = ArticleSerializer(query_set, many=True)
        return Response(serializer.data)



#% genric views with mixins
class ArticleGenericMixinView(
    generics.GenericAPIView,
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    lookup_field = 'id'

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request,id)


# $ the above class can also be defined as below
# class GenericMixinView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):

