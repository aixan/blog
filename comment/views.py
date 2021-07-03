from rest_framework import viewsets

from comment.models import Comment
from comment.forms import CommentSerializer
from comment.permissions import IsOwnerOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
