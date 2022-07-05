from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class SignUpForm(UserCreationForm):


    #username = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class':'form-control'}))
    #password1 = forms.PasswordInput()
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
 
    class Meta:
        model = User
        fields = ('username','data_nascimento','password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        #self.fields['data_nascimento'].widget.attrs['class'] = 'form-control'

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('foto',)
        widget ={
                #'name':forms.TextInput(attrs={'class':'form-control'}),
                #'birth_date':forms.DateInput(attrs={'class':'form-control'}),
                #'detalhes':forms.TextInput(attrs={'class':'form-control'})
                }