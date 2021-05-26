from django.shortcuts import render
from rest_framework import generics,permissions, serializers
from .models import Post
from .serializers import PostSerializer

class PostListView(generics.ListAPIView):
    permission_classes=[permissions.AllowAny]
    queryset=Post.objects.all()
    serializer_class=PostSerializer

