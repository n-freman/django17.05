from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'image', 'description', 'price',]


class SearchForm(forms.Form):
    title = forms.CharField(required=False)
    min_price = forms.IntegerField(required=False, initial=0)
    max_price = forms.IntegerField(required=False)
