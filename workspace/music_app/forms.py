from django.contrib.auth.models import User
from django import forms



class UserForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput) # to add the asterisk feature for hiding passwords
    
    # inforamtion about the class you are using
    class Meta:
        model = User
        fields = ['username','email','password']