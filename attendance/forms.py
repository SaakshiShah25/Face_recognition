from django import forms
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.forms import ModelForm
from .models import New
User=get_user_model()

class UserCreationForm(forms.ModelForm):
    pass1=forms.CharField(widget=forms.PasswordInput)
    pass2=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'sapid',
            'department',
        ]

    def clean_password(self):
        pass1=self.cleaned_data.get('pass1')
        pass2=self.cleaned_data.get('pass2')
        if pass1 and pass2 and pass1!=pass2:
            raise forms.ValidationError("Passwords do not match")
        return pass2

    def save(self,commit=True):
        user=super(UserCreationForm,self).save(commit=False)
        user.set_password(self.cleaned_data['pass1'])
        user.username=self.cleaned_data['username']
        user.sapid=self.cleaned_data['sapid']
        user.department=self.cleaned_data['department']

        if commit:
             user.save()

        return user
class NewForm(ModelForm):
    class Meta:
        model=New
        fields=[
            'subject',
            'division',
            'acc',
        ]
        widgets={
            'subject':forms.Select(attrs={'class':'btn btn-secondary dropdown-toggle',
                                          'id':'dropdownMenuButton',}),
            'division':forms.Select(attrs={'class':'btn btn-secondary dropdown-toggle',
                                            'id':'dropdownMenuButton',}),
            'acc':forms.Select(attrs={'class':'btn btn-secondary dropdown-toggle',
                                        'id':'dropdownMenuButton',})
        }
        




