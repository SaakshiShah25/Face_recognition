from django import forms
from django.contrib.auth import get_user_model
from django.db.models import Q

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
            'subject',
            'div',
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
        user.subject=self.cleaned_data['subject']
        user.div=self.cleaned_data['div']
        user.sapid=self.cleaned_data['sapid']
        user.department=self.cleaned_data['department']

        if commit:
             user.save()

        return user





