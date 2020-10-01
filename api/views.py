from django.shortcuts import render
from .serializer import PostsSerializer
from .models import Posts
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import F 

# Create your views here.

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.order_by('-postdate')
    serializer_class = PostsSerializer

    @action(detail=False)
    def boastsonly(self, request):
        boast = Posts.objects.filter(boast=True).order_by('-postdate')
        page = self.paginate_queryset(boast)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return Response(serializer.data)
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roastsonly(self, request):
        roasts = Posts.objects.filter(boast=False).order_by('-postdate')
        serializer = self.get_serializer(roasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def scoresort(self, request):
        scores = Posts.objects.order_by(-(F('upvote') - F('downvote')))
        serializer = self.get_serializer(scores, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        posts = Posts.objects.get(id=pk)
        posts.upvote = F('upvote') + 1
        posts.save()
        return Response({'status': 'upvoteset'})

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        posts = Posts.objects.get(id=pk)
        posts.downvote = F('downvote') + 1
        posts.save()
        return Response({'status': 'downvoteset'})

    @action(detail=True, methods=['post'])
    def add_post(self, request):
        add_post = Posts.objects.create(
                text=request.data.text, 
                boast=request.data.boast
            )
        return Response(add_post)

