from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment, Like
from rest_framework import permissions
from rest_framework import filters
from rest_framework import generics
from rest_framework.response import Response
from notifications.models import Notification


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        feed_data = [
            {
                "id": post.id,
                "author": post.author.username,
                "title": post.title,
                "content": post.content,
                "created_at": post.created_at,
            }
            for post in posts
        ]
        return Response(feed_data)
    
class LikePostView(generics.APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if created:
            # create a notification for the post's author
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,
                    actor = request.user,
                    verb='liked your post',
                    target=post,
                )
            return Response({'message': 'Post liked successfuly!'})
        else:
            return Response({'message': 'you already liked this post.'}, status=400)
        
class UnlikePostView(generics.APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post)
        
        if like.exists():
            like.delete()
            return Response({'message': 'Post unliked successfully!'})
        else:
            return Response({'message': 'You have not liked this post yet.'}, status=400)