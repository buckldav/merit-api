from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from blog.api.serializers import CommentSerializer, CreateCommentSerializer
from blog.models import Comment, Post
from organizations.permissions import HasBlogAPIKey
from organizations.models import BlogAPIKey


class CommentViewSet(mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [HasBlogAPIKey]

    def list(self, request):
        queryset = Comment.objects.filter(
            blog_api_key=BlogAPIKey.objects.get_from_key(HasBlogAPIKey().get_key(request)),
            post=Post.objects.get(url=request._request.build_absolute_uri()))
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        post = Post.objects.get_or_create(url=request._request.build_absolute_uri())[0]
        key = BlogAPIKey.objects.get_from_key(HasBlogAPIKey().get_key(request))
        data["blog_api_key"] = key.id
        data["post"] = post.id
        serializer = CreateCommentSerializer(data=data)

        if serializer.is_valid():
            obj = serializer.create(serializer.validated_data)
            if obj is None:
                return Response({"message": "Reached limit of comments to add."}, status=status.HTTP_403_FORBIDDEN)
            else:
                data = serializer.validated_data
                del data["blog_api_key"]
                data["post"] = data["post"].id
                return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
