from django import forms
from tinymce.widgets import TinyMCE
from humorge.models import FreeBoard, HumorBoard, FreeComment, HumorComment


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

class HumorCommentForm(forms.ModelForm):

    class Meta:
        model = HumorComment
        fields = ['content']
