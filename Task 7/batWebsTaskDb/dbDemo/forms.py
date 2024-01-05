from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}),max_length=30)
    em = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),max_length=200)
    class Meta:
        model = User
        fields = ('username', 'name','em','password1','password2')
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fullname','age','contactno','email','college','branch','sscm','hscm']

# class AddRecordForm(forms.ModelForm):
#     fullname = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Full Name", "class":"form-control"}), label="")
#     age = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Age", "class":"form-control"}), label="")
#     contactno = forms.BigIntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Contact No.", "class":"form-control"}), label="")
#     email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="", max_length=200)
#     college = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"College", "class":"form-control"}), label="", max_length=30)
#     branch = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Branch", "class":"form-control"}), label="",max_length=30)
#     sscm = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"SSC Marks", "class":"form-control"}), label="")
#     hscm = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"HSC Marks", "class":"form-control"}), label="")
#     class Meta:
#         model = Student
#         exclude = ("user",)