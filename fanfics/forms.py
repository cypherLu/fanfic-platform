from pyexpat import model
from django import forms
from .models import Fanfic, Chapter, Profile

class fanficForm(forms.ModelForm):
    class Meta:
        model = Fanfic
        fields = ('cover','title', 'synopsis', 'status','tags','fandoms','categories','language')

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ('chapterName','story')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'country']