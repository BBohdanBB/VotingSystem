from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Candidate
from django.utils import timezone
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Button


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title','description', 'icon')

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # This is crucial.
        helper.layout = Layout(
            Fieldset('Create new post', 'title', 'description','icon'),
        )

        return helper


class CandidateFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(CandidateFormHelper, self).__init__(*args, **kwargs)
        self.form_tag = False
        self.layout = Layout(
            Fieldset("Add new candidate", 'name','description', 'photo',),
        )
        #self.helper = CandidateFormHelper()
        #self.helper[:].wrap(self.layout.fields, wrapper_class="housenumber")

CandidateFormset = inlineformset_factory(
    Post,
    Candidate,
    fields=('name','description', 'photo',),
    extra=2,
    can_delete=True,
)