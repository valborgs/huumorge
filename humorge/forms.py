from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE
from humorge.models import FreeBoard, HumorBoard

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user =super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class FreePostForm(forms.ModelForm):

    class Meta:
        model = FreeBoard
        fields = ['title', 'content']

class HumorPostForm(forms.ModelForm):

    class Meta:
        model = HumorBoard
        fields = ['title', 'content']
