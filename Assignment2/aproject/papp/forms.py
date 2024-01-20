from django import forms
from .models import TaskAddModel
class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskAddModel
        fields = ['title', 'description']


