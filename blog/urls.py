from django.urls import path
from blog import views

urlpatterns = [
    path('add_comment/<slug:post_slug>/', views.add_comment),
    path('get_comment/<slug:post_slug>/', views.get_comment),
    path('posts/', views.get_posts),
    path('posts/<slug:post_slug>/',views.get_blog),
    path('news/', views.get_all_news),
    path('news/<slug:news_slug>/', views.get_detailed_news),
    path('news/add_comment/<slug:news_slug>/', views.add_news_comment),
    path('news/get_comment/<slug:news_slug>/', views.get_news_comment),
]