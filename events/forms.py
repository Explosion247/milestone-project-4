from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    reply_to = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Comment
        fields = ("content",)
