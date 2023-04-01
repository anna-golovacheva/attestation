from rest_framework import serializers

from blog.models import Post, Comment
from blog.validators import ForbiddenWordsValidator


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Comment
        fields = (
            'body',
            'author',
            'created',
            'updated'
        )

    def create(self, validated_data):
        pk = self.context.get('request').path_info.split('/')[-4]
        post = Post.objects.filter(pk=pk).first()
        comment = Comment.objects.create(post=post, **validated_data)
        return comment


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(source='comment_set', many=True, required=False)
    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Post
        fields = (
            'header',
            'body',
            'author',
            'pic',
            'created',
            'updated',
            'comments'
        )


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'header',
            'body',
            'pic',
            'created',
            'updated'
        )

        validators = [ForbiddenWordsValidator(field='header')]


