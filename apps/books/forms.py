from django import forms
from django.forms import ModelForm, Textarea
from .models import Review

class ReviewForm(forms.ModelForm):
    template_name = "books/book/review_add.html"
    class Meta:
        model = Review
        fields = ('comment',)
