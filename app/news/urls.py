from django.contrib import admin
from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
   path('news/', views.NewsListView.as_view()),
   path('news/<int:pk>/', views.NewsDetailView.as_view()),
   path('comments/', views.CommentCreateView.as_view()), 
]
