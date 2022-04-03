from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    # 이것도 확인해야되서, 히든 input을 만들꺼
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')
    # 서버에서 확인
    content = models.TextField(null=False) #입력을 받음

    created_at = models.DateTimeField(auto_now=True) #자동생성