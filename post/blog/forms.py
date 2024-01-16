from django.forms import ModelForm
from django import forms
from .models import Post

class PostsForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image1','image2','image3','image4','body']
        

# class CommentForm(forms.ModelForm):
#     model = Comment
#     fields = '__all__'