from django import forms
from tinymce.widgets import TinyMCE
from humorge.models import FreeBoard, HumorBoard, FreeComment, HumorComment


class FreePostForm(forms.ModelForm):

    class Meta:
        model = FreeBoard
        fields = ['title', 'content']

class HumorPostForm(forms.ModelForm):

    class Meta:
        model = HumorBoard
        fields = ['title', 'content']

class FreeCommentForm(forms.ModelForm):

    class Meta:
        model = FreeComment
        fields = ['content']

class HumorCommentForm(forms.ModelForm):

    class Meta:
        model = HumorComment
        fields = ['content']
