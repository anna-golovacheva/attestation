from rest_condition import Or, And
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from blog.models import Post, Comment
from blog.permissions import PostOrCommentUpdatePermissionManager, PostAppropriateAgePermissionManager
from blog.serializers import PostSerializer, CommentSerializer, UserPostSerializer


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]


class PostCreateAPIView(generics.CreateAPIView):
    permission_classes = [And(PostAppropriateAgePermissionManager, IsAuthenticated)]
    serializer_class = UserPostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [Or(IsAdminUser, PostOrCommentUpdatePermissionManager)]
    serializer_class = UserPostSerializer
    queryset = Post.objects.all()


class PostDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [Or(IsAdminUser, PostOrCommentUpdatePermissionManager)]
    serializer_class = UserPostSerializer
    queryset = Post.objects.all()


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        print(request)
        return super().list(request, *args, **kwargs)


class CommentCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [Or(IsAdminUser, PostOrCommentUpdatePermissionManager)]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [Or(IsAdminUser, PostOrCommentUpdatePermissionManager)]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
