from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        models = News
        fields = ['title', 'content']
