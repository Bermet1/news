from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import News, Comments, Votes

class UserSerializer(serializers.ModelSerializer):
    """Users"""
    class Meta:
        model = User
        fields = ['id', 'username']


class VoteSerializer(serializers.ModelSerializer):
    """Voting"""
    class Meta:
        model = Votes
        fields = ['news', 'value']


class NewsListSerializer(serializers.Serializer):
    """List of News"""

    title = serializers.CharField(max_length=100)
    link = serializers.URLField(max_length=250)

    class Meta:
        model = News
        fields = ['title', 'link'] 


class NewsDetailSerializer(serializers.ModelSerializer):
    """Detail News"""

    class Meta:
        model = News
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """Comments"""
    class Meta:
        model = Comments
        fields = ['content']

class CommentCreateSerializer(serializers.ModelSerializer):
    """Create Comments"""
    class Meta:
        model = Comments
        fields =  "__all__"



