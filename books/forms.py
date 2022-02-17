from cProfile import label
from django import forms
from .models import Comment, RequestBook


class CommentForm(forms.ModelForm):
	""" creat topic for client """
	class Meta:
		""" auth elemans for form"""
		model = Comment
		fields = ['body']
		label = {'body': 'comment type : '}

class RequestForm(forms.ModelForm):
	""" creat topic for client """
	class Meta:
		""" auth elemans for form"""
		model = RequestBook
		fields = ['text_to_admin']
		label = {'text_to_admin': 'send request : '}		



		



