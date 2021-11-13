from blog.models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'content', 'date_created')


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'content', 'blog_api_key', 'post')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
