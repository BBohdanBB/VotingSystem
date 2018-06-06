from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Candidate
from django.utils import timezone


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


class AddPostForm(forms.Form):
    class Meta:
        model = Post
        fields = ('title', 'description', 'icon', 'candName', 'candPhoto', 'candDescription', )
        widgets = {
            'createDate': forms.HiddenInput(),
            'user': forms.HiddenInput(),
            'modifiedDate': forms.HiddenInput(),
            'postId': forms.HiddenInput(),
        }

    def save(self, commit = True):
        post = super(AddPostForm, self).save(commit=False)
        post.createDate = timezone.now()
        post.modifiedDate = timezone.now()
        post.icon = self.cleaned_data['icon']
        post.title = self.cleaned_data['title']
        post.checked = False
        post.description = self.cleaned_data['description']

