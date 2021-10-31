from django.shortcuts import render
from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from .serializers import *
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response


class NewsListView(APIView):
    """List of News"""

    def get(self, request):
        news = News.objects.all()
        serializer = NewsListSerializer(news)
        return Response(serializer.data)

class NewsDetailView(APIView):
    """Detail news"""

    def get(self, request, pk):
        news = News.objects.filter(id=pk)
        serializer = NewsDetailSerializer(news)
        return Response(serializer.data)

class CommentCreateView(APIView):
    """adding comments"""

    def post(self, request):
        comment = CommentCreateSerializer(data=request.data)
        if comment.is_valid():
            comment.save
        return Response(status=201)