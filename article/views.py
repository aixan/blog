from rest_framework import generics, viewsets, filters

from article.models import Article, Category, Tag, Avatar
from article.permissions import IsAdminUserOrReadOnly
from article.forms import CategorySerializer, CategoryDetailSerializer, TagSerializer, AvatarSerializer
from article.forms import ArticleListSerializer, ArticleDetailSerializer, ArticleSerializer, CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        else:
            return CategoryDetailSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = None


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """文章详情视图"""
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]

    # 这个属性不需要了
    # filterset_fields = ['author__username', 'title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = self.queryset
        username = self.request.query_params.get('username', None)

        if username is not None:
            queryset = queryset.filter(author__username=username)

        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer


class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = [IsAdminUserOrReadOnly]
