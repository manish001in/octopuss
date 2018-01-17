from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'required': True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'required':True}))