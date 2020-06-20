from rest_framework import serializers
from . models import Article

class ArticlePostView(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title','discription']