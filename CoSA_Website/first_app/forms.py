from django import forms
from first_app.models import Profile,  Club
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20, required=True)
    
    class Meta():

        model = User
        fields = ('first_name','last_name','username','email','password')
              
         


    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email address is already in use.')
        cleaned_data = super(RegisterForm, self).clean()    
        