from django import forms
from .models import Profile


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name','last_name','email','date_of_birth','photo','about_me')
