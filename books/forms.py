from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
	""" creat topic for client """
	class Meta:
		""" auth elemans for form"""
		model = Comment
		fields = ['body']
		label = {'body': 'comment type : '}
