from rest_framework import serializers
from .models import Article


# !using ModalSerilizer
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


# !using normal serilizer
# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=256)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     content = serializers.TextField()
#     created = serializers.DateTimeField()

#     def create(self, validated_data):
#         return Article.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.content = validated_data.get('content', instance.content)
#         instance.created = validated_data.get('created', instance.created)
#         instance.save()
#         return instance