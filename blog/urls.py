from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostListAPIView, PostCreateAPIView, PostRetrieveAPIView, PostUpdateAPIView, PostDestroyAPIView, \
    CommentListAPIView, CommentCreateAPIView, CommentUpdateAPIView, CommentDestroyAPIView

app_name = BlogConfig.name

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='posts'),
    path('posts/create/', PostCreateAPIView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostRetrieveAPIView.as_view(), name='post_retrieve'),
    path('posts/update/<int:pk>/', PostUpdateAPIView.as_view(), name='post_update'),
    path('posts/destroy/<int:pk>/', PostDestroyAPIView.as_view(), name='post_destroy'),
    path('posts/<int:pk>/comments/', CommentListAPIView.as_view(), name='comments'),
    path('posts/<int:pk>/comments/create/', CommentCreateAPIView.as_view(), name='comment_create'),
    path('posts/comments/update/<int:pk>/', CommentUpdateAPIView.as_view(), name='comment_update'),
    path('posts/comments/destroy/<int:pk>/', CommentDestroyAPIView.as_view(), name='comment_destroy'),
    ]