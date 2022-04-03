from django.db import models
# Create your models here.


class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=200, null=True)

    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} : {self.title}' #이 안에다가 직접 변수를 출력할 수 있음, 몇번 게시판. 몇 번 이름