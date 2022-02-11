from django import forms
from . import models

class MagazaForm(forms.ModelForm):
    class Meta:
        model = models.Magaza
        fields = [
            'name',
            'category',
            ]
class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = [
            'title',
            'price',
            'file',
            'info',
        ]