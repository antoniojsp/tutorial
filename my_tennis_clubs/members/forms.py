from django import forms

class NameForm(forms.Form):
    firstname = forms.CharField(label='Your first name', max_length=100)
    lastname = forms.CharField(label='Your last name', max_length=100)
