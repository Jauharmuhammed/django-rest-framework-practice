from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from django.http.response import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, APIView, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


#% Function based views here.
@api_view(['GET', 'POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def articles_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        # //return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    if request.method == 'POST':
        # // data = JSONParser().parse(request)
        # // serializer = ArticleSerializer(data=data)
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            # // return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # // return JsonResponse(serializer.errors, status=400)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def article_detail(request, pk):
    try:
        article = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)



    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        # // return JsonResponse(serializer.data)
        return Response(serializer.data)


    if request.method == 'PUT':
        # // data = JSONParser().parse(request)
        # // serializer = ArticleSerializer(article, data=data)
        serializer = ArticleSerializer(article, data=request.data)


        if serializer.is_valid():
            serializer.save()
            # // return JsonResponse(serializer.data)
            return Response(serializer.data)
        else:
            # // return JsonResponse(serializer.errors, status=400)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        article.delete()
        # // return JsonResponse('Article deleted successfully', status=204)
        return Response('Article Deleted Successfully', status=status.HTTP_204_NO_CONTENT)


#% class based views
class ArticleAPIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailsAPIView(APIView):
    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, reuquest, id):
        article = self.get_object(id)
        article.delete()
        return Response('Article Deleted Successfully', status=status.HTTP_204_NO_CONTENT)

