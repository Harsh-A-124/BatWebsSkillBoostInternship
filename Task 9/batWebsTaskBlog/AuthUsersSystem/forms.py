from django.contrib.auth.forms import UserCreationForm,UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from BlogDemo.models import UserProfile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditUserForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    # last_login = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control', 'id':'last_login'}))
    # date_joined = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control', 'id':'date_joined'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1 = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2 = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic','bio','website_url','social_media_url')
        widgets ={
            'website_url' : forms.TextInput(attrs={'class':'form-control'}),
            'social_media_url' : forms.TextInput(attrs={'class':'form-control'}),
            'bio' : forms.Textarea(attrs={'class':'form-control'}),
            'profile_pic' : forms.ClearableFileInput(attrs={'class':'form-control'}),
        }

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic','bio','website_url','social_media_url')
        widgets ={
            'website_url' : forms.TextInput(attrs={'class':'form-control'}),
            'social_media_url' : forms.TextInput(attrs={'class':'form-control'}),
            'bio' : forms.Textarea(attrs={'class':'form-control'}),
            'profile_pic' : forms.FileInput(attrs={'class':'form-control'}),
        }