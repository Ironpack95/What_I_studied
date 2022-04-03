from django.forms import ModelForm

from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['image', 'title', 'description'] # 입력으로 받을 꺼