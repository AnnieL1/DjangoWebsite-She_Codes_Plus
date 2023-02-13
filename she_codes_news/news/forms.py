from django import forms
from django.forms import ModelForm
from .models import NewsStory

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content','image',]
        widgets = {
            'pub_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

# class UserForm(UserCreationForm):
#     email = forms.EmailField(required=True) 
    
#     class Meta:
#         model = User
#         fields = ['username', 'First name', 'Last name', 'email', 'password1','password2']

#     def save(self, commit=True):
#         user = super(UserForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user 
