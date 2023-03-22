from rest_framework import serializers
from .models import Post, Comment, News

class PostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'intro','date', 'get_image', 'slug')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'blog', 'date', 'get_image')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'date', 'comment')

class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'intro', 'date', 'get_image', 'slug')

class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'news', 'date', 'get_image')