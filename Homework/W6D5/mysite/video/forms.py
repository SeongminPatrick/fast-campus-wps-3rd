from django import forms

from .models import Category, Video



class CategoryForm(forms.ModelForm):

    class Meta():
        model = Category
        fields = ('name', )


class VideoForm(forms.ModelForm):

    class Meta():
        model = Video
        fields = ('category', 'title', 'address', 'view_count', 'like_count', )
