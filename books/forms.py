from django import forms
from .models import Comment
from .models import Image

class CommentForm(forms.ModelForm):
	""" creat topic for client """
	class Meta:
		""" auth elemans for form"""
		model = Comment
		fields = ['body']
		label = {'body': 'comment type : '}

'''
class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
'''		

