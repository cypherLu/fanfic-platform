from pyexpat import model
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .models import Fanfic, Chapter, Profile

class fanficForm(forms.ModelForm):
    class Meta:
        model = Fanfic
        fields = ('cover','title', 'synopsis', 'status','tags','fandoms','categories','language')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'kilig-form'

        self.helper.layout = Layout(
            Field('cover', css_class='kilig-file'),
            Field('title', css_class='kilig-input'),
            Field('synopsis', css_class='kilig-textarea'),
            Field('status', css_class='kilig-input'),
            Field('tags', css_class='kilig-input'),
            Field('fandoms', css_class='kilig-input'),
            Field('categories', css_class='kilig-input'),
            Field('language', css_class='kilig-input'),
            Submit('submit', 'Submit', css_class='kilig-btn')
        )

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ('chapterName','story')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'kilig-form'

        self.helper.layout = Layout(
            Field('chapterName', css_class='kilig-input'),
            Field('story', css_class='kilig-textarea'),
            Submit('submit', 'Submit', css_class='kilig-btn')
        )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'country']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'kilig-form'

        self.helper.layout = Layout(
            Field('avatar', css_class='kilig-file', id='avatar-input'),
            Field('bio', css_class='kilig-textarea'),
            Field('country', css_class='kilig-input'),
            Submit('submit', 'Save', css_class='kilig-btn')
        )