from .models import Post, Support
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'post_name', 'item', 'description', 'price', 'contact_information', 'tags',)


class SupportForm(ModelForm):
    class Meta:
        model = Support
        fields = ('text',)
