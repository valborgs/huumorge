from django import forms
from tinymce.widgets import TinyMCE
from humorge.models import FreeBoard, HumorBoard, FreeComment, HumorComment


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class FreePostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCEWidget(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = FreeBoard
        fields = ['title', 'content']

class HumorPostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCEWidget(attrs={'cols': 80, 'rows': 30}))

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
