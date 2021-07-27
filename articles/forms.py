from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].label = ""

    class Meta:
        model = Comment
        fields = ('comment',)