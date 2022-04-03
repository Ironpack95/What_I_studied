from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from articleapp.models import Article
from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        # article의 객체가 요청 받은 POST데이터 중에 article_pk라는 데이터를 통해서, 이를 가진 아티클을 지금 만들 아티클의 값으로
        # hidden input이 여기로 온다
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return  reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})

@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return  reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})