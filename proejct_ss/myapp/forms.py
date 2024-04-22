from django import forms
from .models import VideoModel

class VideoUploaderForm(forms.ModelForm):
    content=forms.FileField(widget=forms.ClearableFileInput(attrs={'accept': 'video/*'}))
    class Meta:
        model=VideoModel
        fields=['title', 'content', 'description']

class UpdateVideoForm(forms.ModelForm):
    class Meta:
        model=VideoModel
        fields=['title', 'description']