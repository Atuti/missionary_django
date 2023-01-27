from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer, PostsListSerializer, CommentSerializer, NewsListSerializer, NewsDetailSerializer
from .models import Post, Comment, News

@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()

    serializer = PostsListSerializer(posts, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_blog(request, post_slug):
    post = Post.objects.get(slug = post_slug)

    serializer = PostSerializer(post)

    return Response(serializer.data)


@api_view(['POST'])
def add_comment(request, post_slug):
    data = request.data

    post = Post.objects.get(slug = post_slug)

    comment = Comment.objects.create(post = post, name=data.get('name'), date = data.get('date'), comment=data.get('comment'))

    serializer = CommentSerializer(comment)

    return Response(serializer.data)

@api_view(['GET'])
def get_comment(request, post_slug):
    post = Post.objects.get(slug = post_slug)

    comments = post.comments.all()

    serializer = CommentSerializer(comments, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_all_news(request):
    news = News.objects.all()

    serializer = NewsListSerializer(news, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_detailed_news(request, news_slug):
    news = News.objects.get(slug = news_slug)

    serializer = NewsDetailSerializer(news)

    return Response(serializer.data)

@api_view(['POST'])
def add_news_comment(request, news_slug):
    data = request.data

    news = News.objects.get(slug = news_slug)

    comment = Comment.objects.create(news = news, name=data.get('name'), date = data.get('date'), comment=data.get('comment'))

    serializer = CommentSerializer(comment)

    return Response(serializer.data)

@api_view(['GET'])
def get_news_comment(request, news_slug):
    news = News.objects.get(slug = news_slug)

    comments = news.comments.all()

    serializer = CommentSerializer(comments, many=True)

    return Response(serializer.data)