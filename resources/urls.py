from django.urls import path
from resources import views

urlpatterns = [
    path('ebooks/', views.get_all_ebooks),
    path('first-ebook/', views.get_first_ebook)
]