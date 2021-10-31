from django.shortcuts import render
from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from .serializers import *
from .models import *


# class CreateVoteView(generics.CreateAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = VoteSerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)