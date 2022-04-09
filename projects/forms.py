
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Rating

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design_rating', 'usability_rating', 'content_rating']
