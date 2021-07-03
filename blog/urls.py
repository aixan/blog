# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from article import views
from comment.views import CommentViewSet
from user.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router = DefaultRouter()
router.register(r'article', views.ArticleViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'tag', views.TagViewSet)
router.register(r'avatar', views.AvatarViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    # drf 自动注册路由
    # path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# 把媒体文件的路由注册了
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
