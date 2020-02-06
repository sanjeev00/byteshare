from django import forms



class LoginForm(forms.Form):

    user = forms.CharField(label='your name', max_length=10)
    pas = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.Form):
    user = forms.CharField(max_length=30)
    pas  = forms.CharField(widget=forms.PasswordInput)
    first = forms.CharField(max_length=20)
    last = forms.CharField(max_length=20)

