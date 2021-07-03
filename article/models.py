from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from markdown import Markdown


class Category(models.Model):
    """文章分类"""
    title = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Tag(models.Model):
    """文章标签"""
    text = models.CharField(max_length=30)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-id']


class Avatar(models.Model):
    content = models.ImageField(upload_to='avatar/%Y%m%d')


# 博客文章 model
class Article(models.Model):
    # 标题图
    avatar = models.ForeignKey(Avatar, null=True, blank=True, on_delete=models.SET_NULL, related_name='article')
    # 标题
    title = models.CharField(max_length=100)
    # 分类
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name='articles')
    # 标签
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles')
    # 正文
    body = models.TextField()
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='articles')

    # 新增方法，将 body 转换为带 html 标签的正文
    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_body = md.convert(self.body)
        # toc 是渲染后的目录
        return md_body, md.toc

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
