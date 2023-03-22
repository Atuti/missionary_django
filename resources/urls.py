from django.urls import path
from resources import views

urlpatterns = [
    path('ebooks/', views.get_all_ebooks),
    path('first-ebook/', views.get_first_ebook),
    path('links/', views.get_links),
    path('home-links/', views.get_home_links),
    path('study-video-links/', views.get_study_links),
    path('study-guides/', views.get_study_guides),
]