from django import forms
from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['name_comment', 'email_comment', 'message_comment']