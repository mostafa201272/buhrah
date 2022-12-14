from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisteration(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", "last_name","username", "email", "password1", "password2"]
    

    def __init__(self, *args, **kwargs):
        super(UserRegisteration, self).__init__(*args, **kwargs)

        # First name Field
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['first_name'].widget.attrs['required'] = 'true'
        
        # Last name Field
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['last_name'].widget.attrs['required'] = 'true'

        # Username Field
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].widget.attrs['required'] = 'true'

        # Email Field
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['required'] = 'true'

        # Password Field
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['required'] = 'true'

        # confirm password Field
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        self.fields['password2'].widget.attrs['required'] = 'true'