from django.urls import path
from rainbow import views

urlpatterns = [
    path('send_question/', views.send_question),
    path('send_testimony/', views.send_testimony),
    path('send_prayer/', views.send_prayer_request),
    path('send_email/', views.send_email),
]