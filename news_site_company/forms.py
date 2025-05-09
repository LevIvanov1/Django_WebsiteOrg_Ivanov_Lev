from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import News

class RegisterForm(UserCreationForm):
        email = forms.EmailField(required=True)

class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

class CommentForm(forms.Form):
        text = forms.CharField(label='Ваш комментарий', widget=forms.Textarea)

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image']