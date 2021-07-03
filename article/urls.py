from django.urls import path
from article import views

app_name = 'article'


urlpatterns = [
    path('<int:pk>', views.ArticleDetail.as_view(), name='datail'),
]
