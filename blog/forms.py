from .models import Comment, Article
from django import forms
from tinymce.widgets import TinyMCE


class TinyMCEWidget(TinyMCE):
	def use_required_attribute(self, *args):
		return False


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('content',)
    


class ArticleForm(forms.ModelForm):
	content = forms.CharField(
		widget=TinyMCEWidget(
			attrs={'required': False, 'cols': 30, 'rows': 10}
		)
	)
	class Meta:
		model = Article
		fields = '__all__'
