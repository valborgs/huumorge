from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE
from humorge.models import FreeBoard, HumorBoard, FreeComment, HumorComment

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nickname = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "nickname", "email", "password1", "password2")

    def save(self, commit=True):
        user =super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.nickname = self.cleaned_data["nickname"]
        if commit:
            user.save()
        return user

class FreePostForm(forms.ModelForm):
    content = forms.CharField(max_length=None, widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = FreeBoard
        fields = ['title', 'content']
        widgets = {'content': TinyMCE()}

class HumorPostForm(forms.ModelForm):
    content = forms.CharField(max_length=None, widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = HumorBoard
        fields = ['title', 'content']
        widgets = {'content': TinyMCE()}

class FreeCommentForm(forms.ModelForm):

    class Meta:
        model = FreeComment
        fields = ['content']
