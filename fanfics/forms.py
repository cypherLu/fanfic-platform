from pyexpat import model
from django import forms
from .models import Fanfic, Chapter, Profile

class fanficForm(forms.ModelForm):
    class Meta:
        model = Fanfic
        fields = ('cover','title', 'synopsis', 'status','tags','fandoms','categories','language')
        widgets = {
            'cover': forms.ClearableFileInput(attrs={'class': 'kilig-file'}),
            'title': forms.TextInput(attrs={'class': 'kilig-input'}),
            'synopsis': forms.Textarea(attrs={'class': 'kilig-textarea'}),
            'status': forms.Select(attrs={'class': 'kilig-input'}),
            'tags': forms.TextInput(attrs={'class': 'kilig-input'}),
            'fandoms': forms.TextInput(attrs={'class': 'kilig-input'}),
            'categories': forms.Select(attrs={'class': 'kilig-input'}),
            'language': forms.Select(attrs={'class': 'kilig-input'}),
        }

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ('chapterName','story')
        widgets = {
            'chapterName': forms.TextInput(attrs={'class': 'kilig-input'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'country']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={
            'class': 'kilig-file',
            'id': 'avatar-input'
            }),
            'bio': forms.Textarea(attrs={'class': 'kilig-textarea'}),
            'country': forms.Select(attrs={'class': 'kilig-input'}),
        }