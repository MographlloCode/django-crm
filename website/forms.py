from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    ''' User Creation Form '''
    
    first_name = forms.CharField(max_length=100, label='First Name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Input your first name here'}))
    last_name = forms.CharField(max_length=100, label='Last Name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Input your last name here'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Input your email here'}) )
     
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = 'Username'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Your username goes here.'
        
        self.fields['password1'].label = 'Type your password'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Your password goes here.'
        
        self.fields['password2'].label = 'Repeat the password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Your password goes here.'